import requests
import pandas as pd

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

# count = 1
# while count <  10:
#     response = requests.get("https://lldev.thespacedevs.com/2.3.0/astronauts/" + str(count))
#     astronaut = response.json()
#     agency = astronaut['agency']
#     print("Name: " + astronaut['name'] + "\nAgency: " + agency['name'] + "\nBio: " + astronaut['bio'] + "\n")
#     count += 1


# api_url = "https://lldev.thespacedevs.com/2.3.0/astronauts"

# try:
#     response = requests.get(api_url)
#     response.raise_for_status()
#     data = response.json()
#     print("Successfully retrived data:")
#     print(data)
# except requests.exceptions.RequestException as e:
#     print(f"Error fetching data: {e}")

api_url = "https://lldev.thespacedevs.com/2.3.0/astronauts"

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    print(df.head())
else:
    print(f"Failed to fetch data: {response.status_code}")