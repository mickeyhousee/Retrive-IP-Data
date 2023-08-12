#!/usr/bin/python3
#MADE BY: mickeyhousee
#import readline
import requests
import json
import os
import re # Regular Expressions
import csv # CSV Files



# Menu
def menu():
    print("1. Export data from a csv file")
    print("2. Manually write the ips and save them in a json")
    print("0. Exit program")

# Menu for import_csv function
def menu_import_csv():
    while True:
        option = ''
        print("Menu:")
        print("1. Use default CSV file location")
        print("2. Enter custom CSV file location")
        print("3. Exit")
        try:
            option=int(input("Enter your choice (1/2/3): "))
        except ValueError:
            #readline.clear_history()
            print('')

        # OPTION 1
        if option == 1:
            csv_file_path = 'ips.csv'  
            prepare_csv(csv_file_path)
        elif option == 2:
            print(r'Example of usage: C:\Users\User\Desktop\ips.csv')
            csv_file_path = input('Enter the full path of .csv File: ')
            prepare_csv(csv_file_path)
        elif option == 3:
            break
        else:
            #readline.clear_history()
            print('Invalid option. Please enter a number between 0 and 2.')



# Prepare CSV FILE
def  prepare_csv(csv_file_path):
    ips = []

    #Read ips from csv file
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Jump header
        for row in csv_reader:
            if len(row) > 0:  # Check if the row has elements
                ips.append(row[0])  # Assuming the IP is in the first column

    print("List of IP's:", ips)

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


# Verify if is a valid IP with regular expressions
def is_valid_ip(ip):
    # \d -  Matches any digit character (0-9).
    # {1,3} -  Match between 1 and 3 of the preceding token.
    # \. -  Matches a "." character (char code 46).
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    return re.match(pattern, ip)


# Function ip_manual
def ip_manual ():
    query = input('Enter the IP: ')
    if not is_valid_ip(query):
        print("Invalid IP format. Please enter a valid IP address.")
        return
    json_directory = "JSON_DATA"
    if not os.path.exists(json_directory):
        os.makedirs(json_directory)
    base_url = "http://ip-api.com/json/"+query+"?fields=status,message,continent,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,reverse,mobile,proxy,hosting,query"
    result= requests.get(base_url)
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



# Main
if __name__=='__main__':
    while(True):
        menu()
        opcao =''
        try:
            opcao=int(input())
        except:
            #readline.clear_history()
            print('Wrong input. Please enter a number ...')
        if opcao == 1:
            menu_import_csv()
            
        elif opcao == 2:
            ip_manual()
        elif opcao == 0:
            #readline.clear_history()
            exit("Leaving...")
        else:
            #readline.clear_history()
            print('Invalid option. Please enter a number between 0 and 2.')

