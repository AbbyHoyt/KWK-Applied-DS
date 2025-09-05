import requests
import pandas as pd

api_url = "https://ll.thespacedevs.com/2.3.0/astronauts/?ordering=-time_in_space&is_human=true&limit=100"
response = requests.get(api_url)
astronaut_data = []

while api_url:
    try:
        response = requests.get(api_url)
        response.raise_for_status() 
        data = response.json()
        astronaut_data.extend(data['results'])
        api_url = data.get('next')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        break

df = pd.json_normalize(astronaut_data, sep = '_')
data_to_keep = ['id', 'name', 'status_name', 'type_name', 'agency_name', 'age', 'date_of_birth', 'date_of_death', 'nationality']
df_final = df.reindex(columns = data_to_keep)
df_final.to_csv('astronaut_data_cleaned_v2.csv', index = False, encoding = 'utf-8')
