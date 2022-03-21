from typing import List

from decouple import config
from tweepy.models import Status
import tweepy
import traceback
import datetime


class TwitterHelper:

    def __init__(self):
        self.api = None

    def connect(self):
        api_key = config("TWITTER_API_KEY")
        api_secrets = config("TWITTER_API_KEY_SECRET")
        access_token = config("TWITTER_ACCESS_TOKEN")
        access_secret = config("TWITTER_ACCESS_TOKEN_SECRET")

        auth = tweepy.OAuthHandler(api_key, api_secrets)
        auth.set_access_token(access_token, access_secret)

        self.api = tweepy.API(auth)

        try:
            self.api.verify_credentials()
            print('Successful Authentication')
        except Exception:
            traceback.print_exc()
            raise

    def user_timeline(self) -> List[Status]:
        tweets_list = []

        tweets = tweepy.Cursor(
            self.api.user_timeline,
            user_id=config('TWITTER_USER_NAME'),
            include_rts=False,
            exclude_replies=True,
            # Necessary to keep full_text. Otherwise, only the first 140 words are extracted
            tweet_mode='extended'
        ).items(100)

        today = datetime.datetime.now()
        days_ago = 1
        since_date = (today - datetime.timedelta(days_ago)).date()
        for tweet in tweets:
            if tweet.created_at.date() >= since_date:
                tweets_list.append(tweet)

        return tweets_list

    def update_status(self, status):
        try:
            self.api.update_status(status=status)
            print('Tweet posted')
        except Exception:
            traceback.print_exc()
            raise
