import requests
import pandas as pd

api_url = "https://ll.thespacedevs.com/2.3.0/astronauts/?ordering=-time_in_space&is_human=true&limit=100"

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    df.to_csv('astronaut_data.csv')
    print(df.head())
else:
    print(f"Failed to fetch data: {response.status_code}")
