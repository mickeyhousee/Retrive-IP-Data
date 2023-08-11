#!/usr/bin/python3

#MADE BY: mickeyhousee


import requests
import json
import os

query = input('Enter the IP: ')
json_directory = "JSON_DATA"
base_url = "http://ip-api.com/json/"+query+"?fields=status,message,continent,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,reverse,mobile,proxy,hosting,query"
result= requests.get(base_url)

#Check if result is ok

if result.status_code == 200:
    # Parse the json data from the result content
    json_data = result.json()
    
    #Specify the local file where you want to store the JSON data
    local_file_json = os.path.join(json_directory, query + ".json")

        # Write the JSON data to the local file
    with open(local_file_json, "w") as json_file:
        json.dump(json_data, json_file, indent=4)
    
    print("JSON data stored locally!")
else:
    print("Error fetching JSON data. Status code:", result.status_code)

