import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "ZVMWNAQG2UVCAGOR"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "4e7a8d77891a41b3982a1e76cb074800"

TWILLIO_SID = "AC6d2792e2305e4384c2ecc9e2982a8f71"
TWILLIO_AUTH_TOKEN = "b39b62c6bb7bf76600896ab5a9c9ef5b"

up_down = None


def send_message(text: str):
    client = Client(TWILLIO_SID, TWILLIO_AUTH_TOKEN)

    message = client.messages.create(
        body=text,
        from_='+19704429461',
        to='+5511956492900'
    )
    print(message.sid)


def get_stock_percentage() -> float:
    global up_down
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
    if stock_price_difference > 0:
        up_down = "🔺"
    else:
        up_down = "🔻"

    stock_percentage = (stock_price_difference / first_stock_price) * 100

    return stock_percentage


def get_news() -> str:
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }
    news_response = requests.get(NEWS_ENDPOINT, news_params)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]
    return news_data[:3]


percentage = get_stock_percentage()
if percentage >= 1:
    articles = get_news()

    formatted_articles = [
        f"\n{STOCK_NAME}: {up_down}{percentage:.2f}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for
        article in articles]

    for msg in formatted_articles:
        send_message(msg)

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
