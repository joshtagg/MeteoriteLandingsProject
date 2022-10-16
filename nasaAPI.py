from unicodedata import name
import requests
import json

import matplotlib.pyplot as plt
import scipy.io as sio
import scipy.interpolate as interpolate
import numpy as np

response = requests.get("https://data.nasa.gov/resource/gh4g-9sfh.json")
#print(response.status_code)
'''
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())
'''
#name = response.json()['name']
#print(name)

meteorites = json.loads(response.text)

# print one meteorite from .json
print(meteorites[:1])

#name and latitude
name_list = {}
lat_list = {}
i = 0
for meteorite in meteorites:
    name_list[i] = meteorite["name"]
    lat_list[i] = meteorite.get('reclat')
    i = i+1

print(name_list[0])
print(name_list[1])
print(name_list[2])
print(lat_list[0])
print(lat_list[1])
print(lat_list[2])

print(name_list[100])
print(lat_list[100])