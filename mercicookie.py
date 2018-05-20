# coding: utf-8
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from itertools import chain
from os import environ
import logging

try:
    from http import client
except ImportError:
    import httplib as client

from errbot import BotPlugin, botcmd
import requests

CONFIG_TEMPLATE = {
    'MERCICOOKIE_API_TOKEN': environ.get('MERCICOOKIE_API_TOKEN', 'your_api_token_here'),
    'MERCICOOKIE_API_EMAIL': environ.get('MERCICOOKIE_API_EMAIL', 'your_api_email_here')
}

MERCICOOKIE_API_ROOT = 'https://www.mercicookie.com/api/v1'
MERCICOOKIE_OFFERS_MAPPING = {
    '6': 7,
    '12': 6,
    '16': 5
}


class MerciCookie(BotPlugin):
    """
    Basic MerciCookie API Err integration
    """

    def get_configuration_template(self):
        """
        Defines the configuration structure this plugin supports
        """
        return CONFIG_TEMPLATE

    def configure(self, configuration):
        if configuration is not None and configuration != {}:
            config = dict(chain(CONFIG_TEMPLATE.items(),
                                configuration.items()))
        else:
            config = CONFIG_TEMPLATE
        super().configure(config)
        return

    @botcmd(split_args_with=';')
    def order(self, message, args):
        """
        Order cookies right from your chat. Choose between 6, 12 or 16 cookies packs.
        """
        if len(args) != 4 or ';' not in str(message):
            return 'Oops, Did you ask me something? Try something like this: !order 6; Jean Dupont, 42 Rue de Londres, Paris; 0123456789; Enjoy these cookies xoxo'

        if args[0] not in MERCICOOKIE_OFFERS_MAPPING.keys():
            return 'Oops! I can only order packs of 6, 12 or 16 cookies.'

        try:
            response = requests.post(
                f'{MERCICOOKIE_API_ROOT}/orders',
                headers={
                    'Authorization': f"Token token=\"{self.config['MERCICOOKIE_API_TOKEN']}\", \
                                             email=\"{self.config['MERCICOOKIE_API_EMAIL']}\""
                },
                json={
                    "recipient_address": args[1],
                    "recipient_phone_number": args[2],
                    "message": args[3],
                    "offer_id": MERCICOOKIE_OFFERS_MAPPING[args[0]]
                }
            )
        except:  # FIXME: we might handle that better...
            return 'Err! Something went wrong :-('

        if response.status_code == 201:
            return 'Yummy! Your cookies are on their way.'

        return 'Err! Something went wrong :-('
