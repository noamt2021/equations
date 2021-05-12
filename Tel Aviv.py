import requests
import json
import re

#Get the response from Geocode:
def Geocode_response(api_key, address):
    url="https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (address,api_key)
    try:
        response = requests.get(url)
        if not response.status_code == 200:
            print("HTTP error, try another url",response.status_code)
        else:
            try:
                response_data = response.json()
            except:
                print("Response not in valid JSON format")
    except:
        print("Something went wrong with requests.get")
    return response_data

# Get the response from Distance Matrix: 
def DistanceM_response(api_key, origin, destinations):
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins={origin}&destinations={destinations}&key={api_key}"
    try:
        response = requests.get(url)
        if not response.status_code == 200:
            print("HTTP error, try another url",response.status_code)
        else:
            try:
                response_data = response.json()
            except:
                print("Response not in valid JSON format")
    except:
        print("Something went wrong with requests.get")
    return response_data

#Read the cities list and make dictionary
def dest(path):
    with open(path, encoding = 'utf-8') as cities:
        file = cities.read()
    file = file.splitlines()
    dests = str(file[0])
    for string in file[1:]:
        dests += ('|' + str(string))
    return dests

# Convert days to hours if the duration is displayed by days
def convertDays(duration):
    duration = duration.split()
    days = int(duration[0])
    hours = int(duration[2]) + (24 * days)
    duration_hours = f'{hours} hours'
    return duration_hours

# Create the desired dictionary:
# Enter Distance Matrix API's response
# Return a dictionary with keys as address's and values as tuple(distance, duration, longitude , latitude)
def createDict(DistanceM_response):
    my_dict = {}
    temp = 0
    for dest in DistanceM_response['destination_addresses']:
        distance = DistanceM_response['rows'][0]['elements'][temp]['distance']['text']
        duration = DistanceM_response['rows'][0]['elements'][temp]['duration']['text']
        if re.search('day', duration):
            duration = convertDays(duration)
        lng = Geocode_response(api_key, dest)['results'][0]['geometry']['location']['lng']
        lat = Geocode_response(api_key, dest)['results'][0]['geometry']['location']['lat']
        my_dict[dest] = (distance, duration, lng, lat)
        temp += 1
    return my_dict
       
def printDict(dict1):
    for dest in dict1:
        distance = dict1[dest][0]
        duration = dict1[dest][1]
        lng = dict1[dest][2]
        lat = dict1[dest][3]
        print(f'Destination: {dest}\nDistance: {distance}\nDuration: {duration}\nLongitude: {lng}\nLatitude: {lat}\n')

path = r'C:\Users\Noam Taichman\Desktop\phython\dests.txt'
destinations = dest(path)
api_key = 'Api from my text file' 
origin = 'Tel Aviv'
DistanceM_response = DistanceM_response(api_key, origin, destinations)
desired_dict = createDict(DistanceM_response)

printDict(desired_dict)

