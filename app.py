"""Twitter bot"""
from flask import Flask, request, render_template, redirect, flash, jsonify, session
app = Flask(__name__)

import tweepy
import secret

from bs4 import BeautifulSoup
import requests
import json
import datetime

today = datetime.datetime.today()

# auth = tweepy.OAuthHandler(secret.CONSUMER_KEY, secret.CONSUMER_SECRET)
# auth.set_access_token(secret.ACCESS_KEY, secret.ACCESS_SECRET)
# api = tweepy.API(auth)

# api.update_status("Another tweet from Becky's laptop")

response = requests.get(f'https://api.weatherbit.io/v2.0/current?city=Raleigh,NC&key={secret.WEATHER_API_KEY}')
data = response.json()
print("***************", today)

# funcs to pull data out of request
# func to determine time of when to tweet