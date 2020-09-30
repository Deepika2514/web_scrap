# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 18:06:14 2020

@author: Deepika
"""

import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import twitter_credentials



# Authenticate
#auth = tweepy.OAuthHandler(KEY, SECRET_KEY)
#auth.set_access_token(KEY, SECRET_KEY)

# Configure to wait on rate limit if necessary
#api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=False)

# Hashtag list
#lst_hashtags = ["#got", "#gameofthrones"]

class TwitterStreamer():
    """
    Class for streaming and processing live tweets
    """
    def stream_tweets(self,fetched_tweets_filename,hash_tag_list):
        
        # This handles twitter authentication and connection to twitter streaming API
        # Make an instance of the class
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY,twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN,twitter_credentials.ACCESS_TOKEN_SECRET)
     
        # Start streaming
        stream = Stream(auth, listener)#, tweet_mode='extended')
        stream.filter(track=hash_tag_list)

# Listener class
class StdOutListener(StreamListener):
    """
    This is a basic listener class that just prints received tweets to stdout
    """
    def __init__(self,fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        # When receiveing a tweet: send it to pubsub
        #write_to_pubsub(reformat_tweet(data._json))
        try:
            #print(data)
            with open(self.fetched_tweets_filename,'a+') as file:
                file.write(data)
            return True
        except BaseException as e:
            print("Error on data: %s" % str(e))
        return True
    
    def on_error(self, status):
#        if status == 420:
#            print("rate limit active")
#            return False
        print(status)
        
if __name__=="__main__":         
     hash_tag_list = ['hiring','Hiring','recruitment','drive','internship','job']
     fetched_tweets_filename = "tweets.json"
     
     twitter_streamer = TwitterStreamer()
     twitter_streamer.stream_tweets(fetched_tweets_filename,hash_tag_list)