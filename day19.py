# Request library

# import requests
# url = "https://sdp-prem-prod.premier-league-prod.pulselive.com/api/v1/competitions/8/teams?_limit=60"

# r = requests.get(url = url)
# if (r.status_code == 200):
#     response = r.json()
#     print(type(response))
#     print(response.keys())
#     result = response['data']
#     print(type(result))
#     final_data = result
#     for i in final_data:
#         print(i['name'],i['stadium'])

import csv
import requests

URL = "https://sdp-prem-prod.premier-league-prod.pulselive.com/api/v1/competitions/8/teams?_limit=60"

try:
    response = requests.get(URL)
    response.raise_for_status()  # Raises exception for 4xx/5xx errors

    data = response.json()

    print("Response Type:", type(data))
    print("Available Keys:", data.keys())

    teams = data.get("data", [])

    print(f"\nTotal Teams: {len(teams)}\n")
    print("-" * 50)

    for team in teams:
        name = team.get("name", "N/A")
        stadium = team.get("stadium", "N/A")

        print(f"Team Name : {name}")
        print(f"Stadium   : {stadium}")
        print("-" * 50)

except requests.exceptions.RequestException as e:
    print(f"Request Error: {e}")
except ValueError:
    print("Invalid JSON response")


print("-"*50)
print("-"*50)

teams_data = response.json().get("data", [])

teams = [
    {
        "name": team.get("name"),
        "stadium": team.get("stadium")
    }
    for team in teams_data
]

for team in teams:
    print(team)


with open("premier_league_teams.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Header
    writer.writerow(["Team Name", "Stadium"])

    # Data
    for team in teams:
        writer.writerow([
            team.get("name"),
            team.get("stadium")
        ])

print("Data saved successfully!")