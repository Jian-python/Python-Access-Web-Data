print('chapter 13 JSON and the REST Architecture')
print('***********part 1***********')
print('1. JavaScript Object Notation - JSON')
# import json
#
# data = '''{
#     "name" : "Chuck",
#     "phone" : {
#         "type" : "intl"
#         "number" : "+1 734 303 4456"
#     },
#     "email" : {
#         "hide" : "yes"
# }
# }'''
#
# info = json.loads(data)
# print('Name:', info["name"])
# print('Hide:', info["email"]["hide"])
print('\n json1.py \n')
import json

data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])

print('\nJson represents data as nested "lists" and "dictionaries"')
print('\n json2 \n')
# Name: Chuck
# Hide: yes

import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

info = json.loads(data)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])

# User count: 2
# Name Chuck
# Id 001
# Attribute 2
# Name Brent
# Id 009
# Attribute 7
print('#####################################################')
print('***********part 2***********')
print('2. Using Application Programming Interfaces')
# Application Programming Interfaces(API)
# services publish the "rule" applications must follow to make use of the service(API)
import urllib.request, urllib.parse, urllib.error
import json

# Note that Google is increasingly requiring keys
# for this API

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
#
# while True:
#     address = input('Enter location: ')
#     if len(address) < 1: break
#
#     url = serviceurl + urllib.parse.urlencode(
#         {'address': address})
#
#     print('Retrieving', url)
#     uh = urllib.request.urlopen(url)
#     data = uh.read().decode()
#     print('Retrieved', len(data), 'characters')
#
#     try:
#         js = json.loads(data)
#     except:
#         js = None
#
#     if not js or 'status' not in js or js['status'] != 'OK':
#         print('==== Failure To Retrieve ====')
#         print(data)
#         continue
#
#     print(json.dumps(js, indent=4))
#
#     lat = js["results"][0]["geometry"]["location"]["lat"]
#     lng = js["results"][0]["geometry"]["location"]["lng"]
#     print('lat', lat, 'lng', lng)
#     location = js['results'][0]['formatted_address']
#     print(location)
print('#####################################################')
print('***********part 3***********')
print('3.  Securing API Requests')
