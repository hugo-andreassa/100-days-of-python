from bs4 import BeautifulSoup
import smtplib
import requests

YOUR_SMTP_ADDRESS = ""
YOUR_EMAIL = ""
YOUR_PASSWORD = ""

BUY_PRICE = 100
PRODUCT_URL = "https://www.amazon.com.br/dp/B07CHRZX7X/?coliid=IV3QR8GGXR67R&colid=37CA451YHVBXX&psc=1&ref_" \
              "=gv_ov_lig_pi_dp "

headers = {
    "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0"
}

response = requests.get(PRODUCT_URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

product_title = soup.find(id="productTitle").text.strip()
product_price = soup.find(name="span", class_="a-price").text.strip()

if product_price < BUY_PRICE:
    message = f"{product_title} is now R${product_price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
