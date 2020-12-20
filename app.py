"""Twitter bot"""
import tweepy
import secret

auth = tweepy.OAuthHandler(secret.CONSUMER_KEY, secret.CONSUMER_SECRET)
auth.set_access_token(secret.ACCESS_KEY, secret.ACCESS_SECRET)
api = tweepy.API(auth)

api.update_status("Test tweet from Becky's laptop")