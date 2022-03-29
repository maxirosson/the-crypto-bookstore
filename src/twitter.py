from typing import List

from decouple import config
from tweepy import Tweet
import tweepy
import traceback
import datetime


def user_timeline(days_ago) -> List[Tweet]:
    result = []

    rcf_3339_format = '%Y-%m-%dT%H:%M:%SZ'
    today = datetime.datetime.now()
    start_time = (today - datetime.timedelta(days_ago)).strftime(rcf_3339_format)

    client = tweepy.Client(bearer_token=config('TWITTER_BEARER_TOKEN'))
    user_id = client.get_user(username=config('TWITTER_USER_NAME')).data.id
    tweets = tweepy.Paginator(client.get_users_tweets,
                              id=user_id,
                              start_time=start_time,
                              exclude=['replies', 'retweets']).flatten()

    for tweet in tweets:
        result.append(tweet)

    return result


def update_status(text):
    try:
        api_key = config("TWITTER_API_KEY")
        api_secrets = config("TWITTER_API_KEY_SECRET")
        access_token = config("TWITTER_ACCESS_TOKEN")
        access_secret = config("TWITTER_ACCESS_TOKEN_SECRET")

        client = tweepy.Client(consumer_key=api_key,
                               consumer_secret=api_secrets,
                               access_token=access_token,
                               access_token_secret=access_secret)
        
        if config("DRY_RUN_ENABLED") == False:
            client.create_tweet(text=text)
            print("Tweet posted:")
            print(text)
        else:
            print("Tweet ignored:")
            print(text)
            
    except Exception:
        traceback.print_exc()
        raise
