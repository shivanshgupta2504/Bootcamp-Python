import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"

# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries.
# e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": os.getenv("STOCK_API"),
}
stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_data = stock_response.json()["Time Series (Daily)"]
stock_list = [value for (key, value) in stock_data.items()]
yesterday_data = stock_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

# Get the day before yesterday's closing stock price
day_before_yesterday_data = stock_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
# Hint: https://www.w3schools.com/python/ref_func_abs.asp
price_diff = yesterday_closing_price - day_before_yesterday_closing_price
sign = ""
if price_diff < 0:
    sign = "🔼"
else:
    sign = "🔽"

# Work out the percentage difference in price between closing price yesterday and closing price the day
# before yesterday.
diff_percent = (abs(price_diff) / yesterday_closing_price) * 100

# STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if diff_percent > 0.1:
    news_params = {
        "apiKey": os.getenv("NEWS_API"),
        "q": COMPANY_NAME,
    }

    news_response = requests.get(os.getenv("NEWS_ENDPOINT"), params=news_params)
    articles = news_response.json()["articles"]

    # Use Python slice operator to create a list that contains the first 3 articles. Hint:
    # https://stackoverflow.com/questions/509211/understanding-slice-notation
    first_three_articles = articles[:3]

    # STEP 3: Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.

    # Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_article_list = [f"{'\n'}{STOCK_NAME}: {sign}{'\n'}Headline: {article['title']}. {'\n'}Brief: {article['description']}" for article in first_three_articles]

    # Send each article as a separate message via Twilio.
    client = Client(os.getenv("ACCOUNT_SID"), os.getenv("AUTH_TOKEN"))
    for article in formatted_article_list:
        message = client.messages.create(
            body=article,
            from_='+12566699553',
            to='+918218827422'
        )

