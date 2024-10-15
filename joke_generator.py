import requests

url = "https://v2.jokeapi.dev/"
response = requests.get(url + "joke/Any?safe-mode")

if response.status_code == 200:
    joke = response.json()
    if joke['type'] == 'ingle':
        print(joke['joke'])
    else:
        print(f"Setup: {joke['setup']}\nDelivery: {joke['delivery']}")
else:
    print("Oops!")