import requests
import datetime
# import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# STOCK PRICES
STOCK_URL = "https://www.alphavantage.co/query"
STOCK_API = "MTA6NK8IDCSCDVRO"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API,
}

# DAYS
today = datetime.date.today()
y_day = today - datetime.timedelta(days=1)
before_y_day = today - datetime.timedelta(days=2)

# NEWS ITEMS
NEWS_URL = "https://newsapi.org/v2/everything"
NEWS_API = "f00e9c618f2b44858f25ccbbe144aeca"
news_parameters = {
    "qInTitle": COMPANY_NAME,
    "from": y_day,
    "to": today,
    "sortBy": "popularity",
    "apiKey": NEWS_API,
}


# SMS CREDENTIALS
account_sid = "ACa9228a24ab57e01084b77f957fbe8fea"
auth_token = "88e54d6820c268ceaafc34b701f5ae3d"

# # STEP 1: Use https://www.alphavantage.co

stock_response = requests.get(url=STOCK_URL, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()

y_day_close = float(stock_data["Time Series (Daily)"][f"{y_day}"]["4. close"])
before_y_day_close = float(stock_data["Time Series (Daily)"][f"{before_y_day}"]["4. close"])

change_in_price = round(y_day_close - before_y_day_close, 4)
percent_change = round((change_in_price/y_day_close) * 100, 1)

price_change: str

if change_in_price < 0:
    price_change = f"🔻{abs(percent_change)}"
else:
    price_change = f"🔺{abs(percent_change)}"

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
if percent_change > 1:

    # print("Get News")
    # # STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_response = requests.get(url=NEWS_URL, params=news_parameters)
    news_response.raise_for_status()
    news = news_response.json()

    for number in range(0, 2):
        news_source = news["articles"][number]["source"]["name"]
        news_title = news["articles"][number]["title"]
        news_description = news["articles"][number]["description"]
        # print(news["articles"][0]["content"])

        message_to_send = f"{STOCK} {price_change}: \nHeadline: {news_title}\nSource: {news_source}\n{news_description}"
        print(message_to_send)
        # # STEP 3: Use https://www.twilio.com
        # Send a separate message with the percentage change
        # and each article's title and description to your phone number.

        client = Client(account_sid, auth_token)

        message = client.messages \
                        .create(
                             body=message_to_send,
                             from_='+17409001474',
                             to='+233205448044'
                         )

        print(f"{message.sid} sent")

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file 
by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
 by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
 coronavirus market crash.
"""
