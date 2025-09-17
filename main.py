import requests
url="http://api.chucknorris.io/jokes/random"
response=requests.get(url)
data=response.json()
print("random joke:",data["value"])