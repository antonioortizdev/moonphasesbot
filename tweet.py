import os
from dotenv import load_dotenv
import tweepy
import moonphase

load_dotenv()

bearer_token = os.environ.get('TWITTER_BEARER_TOKEN')
consumer_key = os.environ.get('TWITTER_API_KEY')
consumer_secret = os.environ.get('TWITTER_API_KEY_SECRET')
access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

def API():
    return tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret, wait_on_rate_limit=True)

def tweet():
    current_moon_phase = moonphase.current()
    current_moon_phase_emoji = moonphase.current_emoji()
    tweet_text = 'Today the Moon Phase will be %s %s' % (current_moon_phase, current_moon_phase_emoji)
    print(tweet_text)
    print(API)
    api = API()
    api.create_tweet(text=tweet_text)

if __name__ == "__main__":
    tweet()