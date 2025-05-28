import requests
from pprint import pprint

API_KEY = '0b4acb254416b48036384f0ba5357ae3'

city = input("Enter your City name..")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_KEY +"&q=" + city


weather_data = requests.get(base_url).json()

pprint(weather_data)