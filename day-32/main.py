import datetime as dt
import random
import smtplib


def send_email(addrs: str, subject: str, msg: str):
    email = "hugo.andreassa@gmail.com"
    password = "okcfnthkjyexifjc"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=addrs,
            msg=f"Subject:{subject}\n\n{msg}")


def get_random_quote():
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
        return random.choice(quotes)


now = dt.datetime.now()
if now.weekday() == 4:
    send_email("hugo.andreassa@gmail.com", "Motivational Quotes", get_random_quote())
