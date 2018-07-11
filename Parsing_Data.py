import requests


url = 'https://api.github.com/user'
response = requests.get(url, headers = {'Authorization': 'Bearer 61e707f34e16a8ac3161e6e3afa54293287c0d3c'})
my_json = response.json()

# Will print all keys in dictionary 
for key in my_json.keys():
	print(key)

# To find value that corresponds to particular key can
# just call dictionary with tht value 

print('Print ID: ', my_json['id'])

	