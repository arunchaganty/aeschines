cp -f ../results/allTweets.csv ../results/allTweetsbkp.csv
python twitterold.py
python twitterRmDups.py ../results/allTweets.csv tweetsnew.csv
rm tweetsnew.csv
