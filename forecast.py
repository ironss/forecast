#! /usr/bin/python
# -*- coding: UTF-8 -*-

import requests

apikey = 'c795da7ea1fadbf5dccbf95d39ce7baa'
location_name = 'Christchurch'
location_lat = '-43.49391'
location_lon = '172.57900'

params = ''
params += 'units=si'

url_fmt = 'https://api.darksky.net/forecast/{apikey}/{lat},{lon}?{params}'
url = url_fmt.format(apikey=apikey, lat=location_lat, lon=location_lon, params=params)
r = requests.get(url)

# Convert the forecast data from JSON to Python
forecast = r.json()

# Generate the report
print('{name} ({lat}, {lon})'.format(name=location_name, lat=location_lat, lon=location_lon))

currently_fmt  = u'{forecast[time]} {forecast[temperature]: 5.1f} °C {forecast[summary]}'
f = forecast['currently']
print(currently_fmt.format(forecast=f))

today_fmt    = u'Today               {forecast[summary]}'
f = forecast['hourly']
print(today_fmt.format(forecast=f))

hourly_fmt   = u'                    {forecast[summary]}'
for i in range(6):
    f = forecast['hourly']['data'][i]
    print(hourly_fmt.format(forecast=f))

thisweek_fmt = u'This week           {forecast[summary]}'
f = forecast['daily']
print(thisweek_fmt.format(forecast=f))

daily_fmt   = u'                    {forecast[summary]}'
for i in range(6):
    f = forecast['daily']['data'][i]
    print(daily_fmt.format(forecast=f))

