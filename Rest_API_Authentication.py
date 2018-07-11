import requests;

url = "https://api.github.com/user"

# Use Authorization tokens to hide Passwords
# Headers will take a dictionary of an authentication key
# Prepend with "Bearer" so we know what kind of key
response = response.get(url, headers = {'Authorization': 'Bearer 61e707f34e16a8ac3161e6e3afa54293287c0d3c'})

print(response.json())
