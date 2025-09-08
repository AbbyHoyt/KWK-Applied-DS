import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("astronaut_data_cleaned_v2.csv")

united_states_of_america_count = 0
russia_count = 0
china_count = 0
japan_count = 0
france_count = 0
denmark_count = 0
canada_count = 0
netherlands_count = 0
kyrgyzstan_count = 0
ukraine_count = 0
belgium_count = 0
united_arab_emirates_count = 0
united_kingdom_count = 0
germany_count = 0
belarus_count = 0
switzerland_count = 0
italy_count = 0
sweden_count = 0
turkey_count = 0
hungary_count = 0
india_count = 0
poland_count = 0
spain_count = 0
israel_count = 0
south_korea_count = 0
malaysia_count = 0
iran_count = 0
south_africa_count = 0
brazil_count = 0
kazakhstan_count = 0
bulgaria_count = 0
saudi_arabia_count = 0
afghan_count = 0
czechia_count = 0
austria_count = 0
slovakia_count = 0
mongolia_count = 0
vietnam_count = 0
romania_count = 0
cuba_count = 0
mexico_count = 0
maltese_count = 0
antigua_and_barbuda_count = 0
pakistan_count = 0
portugal_count = 0
egypt_count = 0
puerto_rico_count = 0
saint_kitts_and_nevis_count = 0
new_zealand_count = 0
panama_count = 0
australia_count = 0
syria_count = 0
norway_count = 0

row = 0
while row < 814:
    current_nationality_array = df.loc[row, 'nationality']

    if "United States of America" in current_nationality_array:
        united_states_of_america_count += 1
    if "Russia" in current_nationality_array:
        russia_count += 1
    if "China" in current_nationality_array:
        china_count += 1
    if "Japan" in current_nationality_array:
        japan_count += 1
    if "France" in current_nationality_array:
        france_count += 1
    if "Denmark" in current_nationality_array:
        denmark_count += 1
    if "Canada" in current_nationality_array:
        canada_count += 1
    if "Netherlands" in current_nationality_array:
        netherlands_count += 1
    if "Kyrgyzstan" in current_nationality_array:
        kyrgyzstan_count += 1
    if "Ukraine" in current_nationality_array:
        ukraine_count += 1
    if "Belgium" in current_nationality_array:
        belgium_count += 1
    if "United Arab Emirates" in current_nationality_array:
        united_arab_emirates_count += 1
    if "United Kingdom" in current_nationality_array:
        united_kingdom_count += 1
    if "Germany" in current_nationality_array:
        germany_count += 1
    if "Belarus" in current_nationality_array:
        belarus_count += 1
    if "Switzerland" in current_nationality_array:
        switzerland_count += 1
    if "Italy" in current_nationality_array:
        italy_count += 1
    if "Sweden" in current_nationality_array:
        sweden_count += 1
    if "Turkey" in current_nationality_array:
        turkey_count += 1
    if "Hungary" in current_nationality_array:
        hungary_count += 1
    if "India" in current_nationality_array:
        india_count += 1
    if "Poland" in current_nationality_array:
        poland_count += 1
    if "Spain" in current_nationality_array:
        spain_count += 1
    if "Israel" in current_nationality_array:
        israel_count += 1
    if "South Korea" in current_nationality_array:
        south_korea_count += 1
    if "Malaysia" in current_nationality_array:
        malaysia_count += 1
    if "Iran" in current_nationality_array:
        iran_count += 1
    if "South Africa" in current_nationality_array:
        south_africa_count += 1
    if "Brazil" in current_nationality_array:
        brazil_count += 1
    if "Kazakhstan" in current_nationality_array:
        kazakhstan_count += 1
    if "Bulgaria" in current_nationality_array:
        bulgaria_count += 1
    if "Saudi Arabia" in current_nationality_array:
        saudi_arabia_count += 1
    if "Afghan" in current_nationality_array:
        afghan_count += 1
    if "Czechia" in current_nationality_array:
        czechia_count += 1
    if "Austria" in current_nationality_array:
        austria_count += 1
    if "Slovakia" in current_nationality_array:
        slovakia_count += 1
    if "Mongolia" in current_nationality_array:
        mongolia_count += 1
    if "Vietnam" in current_nationality_array:
        vietnam_count += 1
    if "Romania" in current_nationality_array:
        romania_count += 1
    if "Cuba" in current_nationality_array:
        cuba_count += 1
    if "Mexico" in current_nationality_array:
        mexico_count += 1
    if "Maltese" in current_nationality_array:
        maltese_count += 1
    if "Antigua and Barbuda" in current_nationality_array:
        antigua_and_barbuda_count += 1
    if "Pakistan" in current_nationality_array:
        pakistan_count += 1
    if "Portugal" in current_nationality_array:
        portugal_count += 1
    if "Egypt" in current_nationality_array:
        egypt_count += 1
    if "Puerto Rico" in current_nationality_array:
        puerto_rico_count += 1
    if "Saint Kitts and Nevis" in current_nationality_array:
        saint_kitts_and_nevis_count += 1
    if "New Zealand" in current_nationality_array:
        new_zealand_count += 1
    if "Panama" in current_nationality_array:
        panama_count += 1
    if "Australia" in current_nationality_array:
        australia_count += 1
    if "Syria" in current_nationality_array:
        syria_count += 1
    if "Norway" in current_nationality_array:
        norway_count += 1

    row = row + 1

nationality_counts = [united_states_of_america_count, 
                      russia_count, 
                      china_count,
                      japan_count,
                      france_count,
                      denmark_count,
                      canada_count,
                      netherlands_count,
                      kyrgyzstan_count,
                      ukraine_count,
                      belgium_count, 
                      united_arab_emirates_count,
                      united_kingdom_count,
                      germany_count,
                      belarus_count,
                      switzerland_count,
                      italy_count,
                      sweden_count,
                      turkey_count,
                      hungary_count,
                      india_count,
                      poland_count,
                      spain_count,
                      israel_count,
                      south_korea_count,
                      malaysia_count,
                      iran_count, 
                      south_africa_count, 
                      brazil_count, 
                      kazakhstan_count, 
                      bulgaria_count, 
                      saudi_arabia_count,
                      afghan_count,
                      czechia_count,
                      austria_count,
                      slovakia_count,
                      mongolia_count,
                      vietnam_count,
                      romania_count,
                      cuba_count,
                      mexico_count,
                      maltese_count,
                      antigua_and_barbuda_count,
                      pakistan_count,
                      portugal_count,
                      egypt_count,
                      puerto_rico_count,
                      saint_kitts_and_nevis_count,
                      new_zealand_count,
                      panama_count,
                      australia_count,
                      syria_count,
                      norway_count]

nationality_names = ["United States of America", 
                     "Russia", 
                     "China",
                     "Japan",
                     "France",
                     "Denmark",
                     "Canada",
                     "Netherlands",
                     "Kyrgyzstan",
                     "Ukraine",
                     "Belgium",
                     "United Arab Emirates",
                     "United Kingdom",
                     "Germany",
                     "Belarus",
                     "Switzerland",
                     "Italy",
                     "Sweden",
                     "Turkey",
                     "Hungary",
                     "India",
                     "Poland",
                     "Spain",
                     "Israel",
                     "South Korea",
                     "Malaysia",
                     "Iran",
                     "South Africa",
                     "Brazil",
                     "Kazakhstan",
                     "Bulgaria",
                     "Saudi Arabia",
                     "Afghan",
                     "Czechia",
                     "Austria",
                     "Slovakia",
                     "Mongolia",
                     "Vietnam",
                     "Romania",
                     "Cuba",
                     "Mexico",
                     "Maltese",
                     "Antigua and Barbuda",
                     "Pakistan",
                     "Portugal",
                     "Egypt",
                     "Puerto Rico",
                     "Saint Kitts and Nevis",
                     "New Zealand",
                     "Panama",
                     "Australia",
                     "Syria",
                     "Norway"]

print(f"Nationality Names: {nationality_names}")
print(f"Nationality Counts: {nationality_counts}")

for i in range(len(nationality_names)):
    print(f"{nationality_names[i]}: {nationality_counts[i]}")

total = 0
for item in nationality_counts:
    total += item
print(f"Accounted nationalities for {total} astronauts.")

sorted_data = sorted(zip(nationality_counts, nationality_names))
sorted_nationality_counts, sorted_nationality_names = zip(*sorted_data)

with plt.style.context('seaborn-v0_8-dark'):
    plt.bar(sorted_nationality_names, sorted_nationality_counts)
    plt.xlabel("Nationality", labelpad = 20, fontsize = 14)
    plt.xticks(rotation = 90, fontsize = 10)
    plt.ylabel("Number of Astronauts", labelpad = 20, fontsize = 14)
    plt.yticks(fontsize = 10)
    plt.title("Nationality vs. Number of of Astronauts", fontsize = 14)
    plt.tight_layout()
    plt.show()

age_counts = df['age'].value_counts()

with plt.style.context('seaborn-v0_8-dark'):
    plt.pie(age_counts.values, labels = age_counts.index, labeldistance = 1.05, rotatelabels = True)
    plt.title("Ages of Astronauts", pad = 25)
    plt.axis("equal")
    plt.show()
