#!/usr/bin/python3

#MADE BY: mickeyhousee


import requests
query = input('Enter the IP: ')

base_url = "http://ip-api.com/json/"+query+"?fields=status,message,continent,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,reverse,mobile,proxy,hosting,query"
result= requests.get(base_url).json()

print(result)