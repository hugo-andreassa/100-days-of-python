import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "ZVMWNAQG2UVCAGOR"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


def get_stock_percentage() -> float:
    # yesterday's closing stock price.
    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "apikey": STOCK_API_KEY
    }
    stock_reponse = requests.get(STOCK_ENDPOINT, stock_params)
    stock_reponse.raise_for_status()
    stock_data = stock_reponse.json()["Time Series (Daily)"]
    stock_data = [stock_data[k] for k in list(stock_data)[:3]]
    # print(stock_data)

    # Yesterday
    first_stock_price = float(stock_data[0]["4. close"])
    # Day before yesterday's
    second_stock_price = float(stock_data[1]["4. close"])
    # Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
    stock_price_difference = abs(first_stock_price - second_stock_price)
    stock_percentage = (stock_price_difference / first_stock_price) * 100

    return stock_percentage


def get_news() -> str:
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": "4e7a8d77891a41b3982a1e76cb074800"
    }
    news_reponse = requests.get(NEWS_ENDPOINT, news_params)
    news_reponse.raise_for_status()
    news_data = news_reponse.json()["articles"]
    articles = news_data[:3]
    print(articles)


percentage = get_stock_percentage()
if percentage >= 1:
    news = get_news()

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
