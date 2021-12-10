from bs4 import BeautifulSoup
import requests

yc_web_page = requests.get("https://news.ycombinator.com/").text

soup = BeautifulSoup(yc_web_page, "html.parser")
all_news = soup.find_all(name="a", class_="titlelink")
for item in all_news:
    print(f"{item.text} - {item.get('href')}")

