# the-crypto-bookstore

# Virtual Environments

Create and activate the virtual environment:
```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

# Install Dependencies

```bash
pip install -r requirements.txt
```

# Configuration

Create a file called `.env` within the project root and configure the following parameters:
<br>`TWITTER_USER_NAME`
<br>`TWITTER_ACCESS_TOKEN`
<br>`TWITTER_ACCESS_TOKEN_SECRET`
<br>`TWITTER_API_KEY`
<br>`TWITTER_API_KEY_SECRET`

You also have to enable OAuth 1.0a to add write permission that is required to post tweets.

# How to run

```bash
python3 src/main.py
```