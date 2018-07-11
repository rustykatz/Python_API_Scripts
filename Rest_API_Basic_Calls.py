# Rusty 2018
# Learning how to do Rest API Calls for python
# Using url: https://jsonplaceholder.typicode.com
# Rest Api is basically a way to interact with a site by telling
# it what to do.
# If an object does not exist you can create it by POST
# If you want information on an object you can use GET 
# If you want to modify an object you can with PUT
# If you want to delete an object you can with delete
import requests

url = 'https://jsonplaceholder.typicode.com/photos'

response = requests.get(url)

# This will print out information of photos from URL by looking at json file
print(response.json())


# Post or a Put: need to add or modify an object
# Must define a payload in form of python dictionary

jsonPayload = {'albumId:1':1,'title':'test','url':'nothing.com',
'thumbnailUrl':'nothing.com'};

# This will show that we added an additional photo to the album
response = requests.post(url,json = jsonPayload);
response.json();
print(response.json())


# This will modify photo 100
url= 'https://jsonplaceholder.typicode.com/photos/100';
repsonse = requests.put(url, json=jsonPayload)
response.json();
print(response.json())

# Delete command 
response = requests.delete(url);
response.json();
print(response.json())




