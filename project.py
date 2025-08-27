import requests

# response = requests.get("http://randomfox.ca/floof")
# print(response.status_code)
# print(response.text)
# print(response.json())
# fox = response.json()
# print(fox['image'])

# response = requests.get("https://lldev.thespacedevs.com/2.3.0/astronauts/?format=json")
# print(response.status_code)
# astronauts = response.json()
# print(astronauts['name'])

# response = requests.get("https://lldev.thespacedevs.com/2.3.0/astronauts/4/?format=json")

# response = requests.get("https://lldev.thespacedevs.com/2.3.0/astronauts/4")
# print(response.status_code)
# astronaut = response.json()
# agency = astronaut['agency']
# print("Name: " + astronaut['name'] + "\nAgency: " + agency['name'])

count = 1
while count <  10:
    response = requests.get("https://lldev.thespacedevs.com/2.3.0/astronauts/" + str(count))
    astronaut = response.json()
    agency = astronaut['agency']
    print("Name: " + astronaut['name'] + "\nAgency: " + agency['name'] + "\nBio: " + astronaut['bio'] + "\n")
    count += 1