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

#print(r)
#print(r.headers)
#print(r.text)

forecast = r.json()

print('{name} ({lat}, {lon})'.format(name=location_name, lat=location_lat, lon=location_lon))

output_current_fmt  = u'{forecast[time]} {forecast[temperature]: 5.1f} °C {forecast[summary]}'
print(output_current_fmt.format(forecast=forecast['currently']))

output_today_fmt    = u'Today               {forecast[summary]}'
print(output_today_fmt.format(forecast=forecast['hourly']))

output_thisweek_fmt = u'This week           {forecast[summary]}'
print(output_thisweek_fmt.format(forecast=forecast['daily']))

#for f in daily['data']:
#   print(f)
#   print(output_fmt.format(forecast=f))

