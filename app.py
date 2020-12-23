"""Twitter bot"""
import tweepy
import secret

from bs4 import BeautifulSoup
import requests

auth = tweepy.OAuthHandler(secret.CONSUMER_KEY, secret.CONSUMER_SECRET)
auth.set_access_token(secret.ACCESS_KEY, secret.ACCESS_SECRET)
api = tweepy.API(auth)

api.update_status("Another tweet from Becky's laptop")



headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
url='https://www.nytimes.com/'
response=requests.get(url,headers=headers)
print(response)