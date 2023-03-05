import config
import requests  # https://docs.python-requests.org/en/latest/
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": config.STOCK_KEY

}
response = requests.get("https://www.alphavantage.co/query?", params=stock_parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
closing_prices = [data[key]["4. close"] for key in list(data)[:2]]
yesterday = float(closing_prices[0])
two_days_ago = float(closing_prices[1])
difference = yesterday - two_days_ago
diff_percent = round((difference / two_days_ago) * 100)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

if abs(diff_percent) > 1:
    # STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_parameters = {
        "q": COMPANY_NAME,
        "searchIn": "title",
        "apiKey": config.NEWS_KEY
    }

    response = requests.get("https://newsapi.org/v2/everything?", params=news_parameters)
    response.raise_for_status()
    data = response.json()["articles"]
    articles = {f"{STOCK}: {up_down}{diff_percent}% \nHeadline: {data[n]['title']}. \nBrief: {data[n]['description']}. \n" for n in range(3)}


    for article in articles:
        account_sid = config.TWILIO_SID  # os.environ['TWILIO_ACCOUNT_SID']
        auth_token = config.TWILIO_TOKEN  # os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                body=article,
                from_=config.TWILIO_NUMBER,
                to=config.MY_NUMBER
    )







## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

