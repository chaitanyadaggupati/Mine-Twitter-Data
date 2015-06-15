import tweepy
from tweepy import OAuthHandler
from keys_tokens import _dict
import json


def login():
    ''' Takes our credentials and logs into Twitter using OAuth. A Tweepy
        api object is returned upon success. '''
    consumer_token = _dict['consumer_key']
    consumer_secret = _dict['consumer_secret']
    access_token = _dict['access_token']
    access_token_secret = _dict['access_secret']

    api = None
    try:
        auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
    except tweepy.TweepError, e:
        print e
    return api


def get_data(api=None):
    if api is None:
        api = login()
    for status in tweepy.Cursor(api.home_timeline).items(10):
        # Process a single status
        print(status.text.encode('utf-8'))

#for friend in tweepy.Cursor(api.friends).items():
#    print(friend.screen_name)


def main():
    get_data()

if __name__ == "__main__":
    main()
