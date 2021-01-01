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

response = requests.get(f'https://api.weatherbit.io/v2.0/current?&lat=24.8983&lon=-77.9318&key={secret.WEATHER_API_KEY}')
data = response.json()
# print("***************", data['data'][0]['wind_spd'])

def pull_facts(data):
    data = data['data'][0]
    wind = ms_to_kns(data['wind_spd'])
    return wind

# funcs to pull data out of request
# func to determine time of when to tweet

def ms_to_kns(ms):
    """converting m/s to knots for wind spd"""
    kns = ms * 1.943844
    return kns


print("****************", )