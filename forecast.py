#! /usr/bin/python3
# -*- coding: UTF-8 -*-

import requests
import datetime as dt

apikey = 'c795da7ea1fadbf5dccbf95d39ce7baa'

location_name = 'Oneroa, Waiheke Island'


loc_url_fmt = 'http://maps.googleapis.com/maps/api/geocode/json?address={addr}'
url = loc_url_fmt.format(addr=location_name)
r = requests.get(url)
location = r.json()
location_lat = location['results'][0]['geometry']['location']['lat']
location_lon = location['results'][0]['geometry']['location']['lng']


params = ''
params += 'units=si'

url_fmt = 'https://api.darksky.net/forecast/{apikey}/{lat},{lon}?{params}'
url = url_fmt.format(apikey=apikey, lat=location_lat, lon=location_lon, params=params)
r = requests.get(url)

# Convert the forecast data from JSON to Python
forecast = r.json()

# Location
print('{name} ({lat}, {lon})'.format(name=location_name, lat=location_lat, lon=location_lon))

# Current situation
currently_fmt  = u'{forecast[datetime]:%Y-%m-%d %H:%M}  {forecast[temperature]: 3.0f} °C  {forecast[summary]}'
f = forecast['currently']
f['datetime'] = dt.datetime.fromtimestamp(f['time'])
print(currently_fmt.format(forecast=f))

# Forecast summary for the rest of today
today_fmt    = u'Today                     {forecast[summary]}'
f = forecast['hourly']
print(today_fmt.format(forecast=f))

# Forecast summary for the rest of the week
thisweek_fmt = u'This week                 {forecast[summary]}'
f = forecast['daily']
print(thisweek_fmt.format(forecast=f))

# Forecast for the next few hours
hourly_fmt   = u'{forecast[datetime]:%H:%M}             {forecast[temperature]: 3.0f} °C  {forecast[summary]}'
print()
for i in range(8):
    f = forecast['hourly']['data'][i]
    f['datetime'] = dt.datetime.fromtimestamp(f['time'])
    print(hourly_fmt.format(forecast=f))

# Forecast for the next few days
daily_fmt   = u'{forecast[datetime]:%a}        {forecast[temperatureMin]: 3.0f} °C {forecast[temperatureMax]: 3.0f} °C  {forecast[summary]}'
print()
for i in range(6):
    f = forecast['daily']['data'][i]
    f['datetime'] = dt.datetime.fromtimestamp(f['time'])
    print(daily_fmt.format(forecast=f))

# Attribution required by license
print()
print('[Powered by Dark Sky|https://darksky.net/poweredby/]')

