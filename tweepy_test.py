import tweepy
import datetime

consumer_key='MCoGpm5kX1zeGrLtrVfbjPxFR'
consumer_secret='u7MZCaOwY7pQljrsH5nILpncuZX4TfDGHT3stcRRjt7aUqo9xt'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)

access_token='412876876-TFGcDhAMBkeZx0gzsqosXpTg4l4Oi16XvT7Tlp7t'
access_token_secret='z0YBqXYlVEqXL5EXwVpl8WNykER9MsNgh004ReZdofxD7'

auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

#post tweets
tweet=str(datetime.datetime.now())+' Wizard Python Test'
api.update_status(status=tweet)

print('Successfully Posted')
print()

#read timelines
public_tweets=api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)