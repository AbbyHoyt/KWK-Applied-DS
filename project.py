import requests

# response = requests.get("http://randomfox.ca/floof")
# print(response.status_code)
# print(response.text)
# print(response.json())
# fox = response.json()
# print(fox['image'])

response = requests.get("https://lldev.thespacedevs.com/2.3.0/astronauts/?format=json")
print(response.status_code)
