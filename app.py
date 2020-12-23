"""Twitter bot"""
import tweepy
import secret

from bs4 import BeautifulSoup
import requests

# auth = tweepy.OAuthHandler(secret.CONSUMER_KEY, secret.CONSUMER_SECRET)
# auth.set_access_token(secret.ACCESS_KEY, secret.ACCESS_SECRET)
# api = tweepy.API(auth)

# api.update_status("Another tweet from Becky's laptop")

URL = 'https://stackoverflow.com/questions/14630288/unicodeencodeerror-charmap-codec-cant-encode-character-maps-to-undefined'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)