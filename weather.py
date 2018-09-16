import praw
import time
import config
import requests
import re
import database_connector
from uszipcode import ZipcodeSearchEngine

COUNTRY = "us"

def get_zip(city, state):
    search = ZipcodeSearchEngine()
    zip = search.by_city_and_state(city, state)
    return zip[0]['Zipcode'] 

def get_weather(zipCode, city):
    URL = "http://api.openweathermap.org/data/2.5/weather?zip={},{}&units=imperial&APPID=c619c39c92b4a826f0d9cd99d15f0d0d".format(zipCode,COUNTRY)
    weatherStatus = requests.get(URL).json()['weather'][0]['main']
    weatherTemp = requests.get(URL).json()['main']['temp']
    weatherString = "Currently in {} the weather is {}, with a tempature of {} degrees F.".format(city,weatherStatus,weatherTemp)
    return weatherString