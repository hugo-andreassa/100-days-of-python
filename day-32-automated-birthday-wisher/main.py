import datetime as dt
import pandas as pd
import smtplib
import random


def setup_letter(name: str):
    letter_number = random.randint(1, 3)
    with open(f"letter_templates/letter_{letter_number}.txt", "r") as file:
        letter_template = file.read().replace("[NAME]", name)
        return letter_template


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


birthdays_dict_list = pd.read_csv("birthdays.csv").to_dict("records")
for birthdays in birthdays_dict_list:
    now = dt.datetime.now()
    if birthdays["month"] == now.month and birthdays["day"] == now.day:
        letter = setup_letter(birthdays["name"])
        print(letter)
        # This func send the email
        # send_email("hugo.andreassa@gmail.com", "Happy Birthday", letter)
