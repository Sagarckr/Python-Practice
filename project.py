# viber api token = 56c060619bf482f0-ef94c4dccb15a0e8-3c3960b2cedc785d
# id = 197BpS6GNRGtGPRmBbMAfA==
# user name = Sagar Sharma
# viber_url = https://chatapi.viber.com/pa/post

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

