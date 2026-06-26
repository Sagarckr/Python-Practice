import requests

url = "https://markets.onlinekhabar.com/smtm/stock_live/sector-performance"

r = requests.get(url)
if r.status_code == 200:
    data = r.json()
    response = data['response']
    positive = []
    negative = []
    for item in response:
        if item['points_change']<0:
            negative.append(item['indices'])
        else:
            positive.append(item['indices'])
    print("Positive -->", len(positive))
    print("Negative -->", len(negative))

print("===================================================")
print("===================================================")

import requests

url = "https://markets.onlinekhabar.com/smtm/stock_live/sector-performance"

r = requests.get(url)

if r.status_code == 200:
    result = r.json()

    positive_sectors = []
    negative_sectors = []

    if isinstance(result, dict):
        data = result["response"]

        for sector in data:
            if sector["percentage_change"] > 0:
                positive_sectors.append(sector) 
            else:
                negative_sectors.append(sector)

        print("Positive Sectors:")
        for sector in positive_sectors:
            print(sector["indices"], sector["percentage_change"])

        print("\nNegative Sectors:")
        for sector in negative_sectors:
            print(sector["indices"], sector["percentage_change"])

    else:
        print("Response is not a dictionary")

else:
    print("Error:", r.status_code)


print("===================================================")
print("===================================================")



import requests

url = "https://markets.onlinekhabar.com/smtm/stock_live/sector-performance"

r = requests.get(url)

if r.status_code == 200:
    result = r.json()

    positive_sectors = {}
    negative_sectors = {}

    data = result["response"]

    for sector in data:
        if sector["percentage_change"] > 0:
            positive_sectors[sector["indices"]] = sector["percentage_change"]
        else:
            negative_sectors[sector["indices"]] = sector["percentage_change"]

    print("Positive Sectors:")
    print(positive_sectors)

    print("\nNegative Sectors:")
    print(negative_sectors)

else:
    print("Error:", r.status_code)


print("===================================================")
print("===================================================")


import requests

url = "https://markets.onlinekhabar.com/smtm/stock_live/sector-performance"

r = requests.get(url)

if r.status_code == 200:
    result = r.json()

    positive_sectors = {}
    negative_sectors = {}

    data = result["response"]

    for sector in data:
        sector_name = sector["indices"]

        if sector["percentage_change"] > 0:
            positive_sectors[sector_name] = sector
        else:
            negative_sectors[sector_name] = sector

    print("=" * 50)
    print("POSITIVE SECTORS")
    print("=" * 50)

    for name, details in positive_sectors.items():
        print(f"""
Sector Name      : {name}
Turnover         : {details['turnover']}
Percentage Change: {details['percentage_change']}
Points Change    : {details['points_change']}
Latest Point     : {details['latest_point']}
Direction        : {details['direction']}
""")

    print("=" * 50)
    print("NEGATIVE SECTORS")
    print("=" * 50)

    for name, details in negative_sectors.items():
        print(f"""
Sector Name      : {name}
Turnover         : {details['turnover']}
Percentage Change: {details['percentage_change']}
Points Change    : {details['points_change']}
Latest Point     : {details['latest_point']}
Direction        : {details['direction']}
""")

else:
    print("Error:", r.status_code)