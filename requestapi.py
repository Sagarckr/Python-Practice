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