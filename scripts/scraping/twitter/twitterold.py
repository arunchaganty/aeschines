import tweepy
from tweepy import OAuthHandler as OAH
import oauth2 as oauth
import urllib2 as urllib
import csv
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = "blIMxhpVum9PqzNix89VjeYdk"
consumer_secret = "Fmz51zDVHogBVXMkZnFuWRoA5WMllq7mRH9iLLqaIMde1khnLZ" 
access_token = "1274455051-eogBNF5foknH40JX96Hfg4noYZPMJm2sWuNbELP"
access_secret = "plpaZORm9w3r9RM1Cn14cYMIALIl37hTma0DPodi4HpqC"

auth = OAH(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

csvFile = open('tweetsnew.csv', 'a')
csvWriter = csv.writer(csvFile)

queries = ["2016Election", "GOP", "election2016", "#Trump2016", "Bernie2016", "#Cruz2016", "#Hillary", "#Cruz", "Marco", "#Trump", "#Bernie", "#USAElection", "#Poll", "#GOPDebate", "#POTUS"]
joinWord = " OR "


api = tweepy.API(auth)
for tweet in tweepy.Cursor(api.search,q=joinWord.join(queries),since="2014-03-13",count=100, lang="en").items():
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
