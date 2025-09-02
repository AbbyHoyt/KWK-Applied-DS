import requests
import pandas as pd
import numpy as np

# Collect
api_url = "https://ll.thespacedevs.com/2.3.0/astronauts/?ordering=-time_in_space&is_human=true&limit=100"

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    df.to_csv('astronaut_data.csv')
    print(df.head())

else:
    print(f"Failed to fetch data: {response.status_code}")

# Clean
results_array = df['results'].values
data_array = np.array(results_array) 

np.savetxt('astronauts_data_results.csv', data_array, fmt='%s', delimiter=',')

# Filter
# # df_filtered = pd.read_csv('astronauts_data_results.csv', sep = ', ')
# df_filtered = pd.read_csv('astronauts_data_results.csv', sep = ',')
# df_filtered.to_csv('final_file.csv')
# print(df_filtered.head())

# df_filtered = pd.read_csv('astronauts_data_results_without_brackets.csv', on_bad_lines='skip')
# df_filtered = df_filtered.drop(['id', 'url'], axis = 1)
# df_filtered.to_csv('astronaut_data_filtered.csv')