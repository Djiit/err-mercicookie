# err-mercicookie - Basic MerciCookie API Err integration

[![Build Status](https://travis-ci.org/Djiit/err-mercicookie.svg?branch=master)](https://travis-ci.org/Djiit/err-mercicookie) [![Coverage Status](https://coveralls.io/repos/github/Djiit/err-mercicookie/badge.svg?branch=master)](https://coveralls.io/github/Djiit/err-mercicookie?branch=master)

Err-MerciCookie is a plugin for [Errbot](https://github.com/errbotio/errbot) that allows you to interact with the [MerciCookie](https://www.mercicookie.com/pages/coffret-cadeau) API. **It requires Python 3.6+**.

## Features

* Order cookies from your favorite chat.

Have an idea ? Open an [issue](https://github.com/Djiit/err-mercicookie/issues) or send me a [pull request](https://github.com/Djiit/err-mercicookie/pulls).

## Usage

### Installation

As admin of an errbot chatbot, send the following command over XMPP:

```
!repos install https://github.com/Djiit/err-mercicookie.git
```

### Commands

Use `!help MerciCookie` to see the available commands and their explanation.

## Configuration

Send configuration commands through chat message to this plugins as in :

```
!plugin config MerciCookie {'MERCICOOKIE_API_TOKEN': 'your_api_token_here', 'MERCICOOKIE_API_EMAIL': 'your_api_email_here',}
```
