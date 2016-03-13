import tweepy
from tweepy import OAuthHandler as OAH
import oauth2 as oauth
import urllib2 as urllib
import csv
from tweepy import Stream
from tweepy.streaming import StreamListener
import logging

logging.basicConfig(filename='tweetsElection.log', format='%(levelname)s:%(asctime)s %(message)s', level=logging.DEBUG)
consumer_key = "blIMxhpVum9PqzNix89VjeYdk"
consumer_secret = "Fmz51zDVHogBVXMkZnFuWRoA5WMllq7mRH9iLLqaIMde1khnLZ" 
access_token = "1274455051-eogBNF5foknH40JX96Hfg4noYZPMJm2sWuNbELP"
access_secret = "plpaZORm9w3r9RM1Cn14cYMIALIl37hTma0DPodi4HpqC"

auth = OAH(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
class MyListener(StreamListener):
    tweetsYet = 0 
    def on_status(self, data):
        try:
            with open('tweetsstream.csv', 'a') as f:
                csvWriter = csv.writer(f)
                csvWriter.writerow([data.created_at, data.text.encode('utf-8')])
                self.tweetsYet += 1
                if self.tweetsYet %100 == 0:
                    logging.info('100 more collected! %s since start.', str(self.tweetsYet))
                return True
        except BaseException as e:
            logging.warning('Error on_data: %s'%str(e))
        return True
 
    def on_error(self, status):
        logging.warning('Error on_data: %s'%status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#2016Election'])

