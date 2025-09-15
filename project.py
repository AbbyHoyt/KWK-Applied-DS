import requests
import pandas as pd

# Filtered API endpoint for LaunchLibrary API v2.3.0.
api_url = "https://ll.thespacedevs.com/2.3.0/astronauts/?ordering=-time_in_space&is_human=true&limit=100"

# Use Requests library to send a GET request to the LaunchLibrary API.
response = requests.get(api_url)

# Array to hold all data acquired from the API endpoint.
astronaut_data = []

while api_url:
    # If request was successful, add data from API to astronaut_data array. 
    try:
        response = requests.get(api_url)
        response.raise_for_status() 
        data = response.json()
        astronaut_data.extend(data["results"])
        api_url = data.get("next")
    # If request was unsuccessful, display error message.
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        break

# Convert astronaut_data array into a pandas DataFrame.
# Use json_normalize to deal with the dictionaries in the dataset.
df = pd.json_normalize(astronaut_data, sep = "_")

# Clean and filter API data, keeping only relevant columns.
data_to_keep = ["id", "name", "type_name", "age", "date_of_birth", "first_flight", "nationality"]
df_final = df.reindex(columns = data_to_keep)

# Turn final, filtered DataFrame into a CSV file.
df_final.to_csv("astronaut_data_updated.csv", index = False, encoding = "utf-8")
