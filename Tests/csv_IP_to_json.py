#!/usr/bin/python3
#MADE BY: mickeyhousee

import csv
import os
import requests
import json


#Open CSV FILE
csv_file_path = 'ips.csv'  
ips = []

#Read ips from csv file
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Jump header
    for row in csv_reader:
        if len(row) > 0:  # Check if the row has elements
            ips.append(row[0])  # Assuming the IP is in the first column

print("List of IP's:", ips)

# Function to store JSON localy
def store_json_locally(url, local_file_path):
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        with open(local_file_path, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)
        print("JSON data stored locally in", local_file_path)
    else:
        print("Error fetching JSON data for", url)

# Directory to store JSON DATA
json_directory = 'JSON_DATA'
if not os.path.exists(json_directory):
    os.makedirs(json_directory)

# Iterate over the list of IPs and run the script for each IP
for ip in ips:
    url = "http://ip-api.com/json/"+ip+"?fields=status,message,continent,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,reverse,mobile,proxy,hosting,query"
    
    # Mount local file path
    local_file_path = os.path.join(json_directory, f"{ip}.json")
    
    # Run the function to store the JSON locally
    store_json_locally(url, local_file_path)
    print("IP added "+ip)