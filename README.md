# [The Crypto Bookstore](https://thecryptobookstore.com/)

[![Tweet](https://github.com/maxirosson/the-crypto-bookstore/actions/workflows/tweet.yml/badge.svg?branch=master)](https://github.com/maxirosson/the-crypto-bookstore/actions/workflows/tweet.yml)

## Virtual Environments

Create and activate the virtual environment:
```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configuration

To use the Twitter API you have to create the following credentials:
<br>`TWITTER_USER_NAME`
<br>`TWITTER_ACCESS_TOKEN`
<br>`TWITTER_ACCESS_TOKEN_SECRET`
<br>`TWITTER_API_KEY`
<br>`TWITTER_API_KEY_SECRET`
<br>`TWITTER_BEARER_TOKEN`

You also have to enable OAuth 1.0a to add write permission that is required to post tweets.

These variables are read using Python-Decouple, so you can set them as environment variables or put them in a `.env` file.

## How to run

```bash
python3 src/main.py
```
