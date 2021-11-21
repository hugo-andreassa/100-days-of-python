import datetime as dt
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


def send_email(addrs: str, subject: str, msg: str):
    email = "hugo.andreassa@gmail.com"
    password = "okcfnthkjyexifjc"

    email_msg = MIMEMultipart('alternative')
    email_msg['Subject'] = subject
    email_msg['From'] = email
    email_msg['To'] = addrs

    with open("email_body.html", "r") as file:
        email_body = file.read().replace("[QUOTE_TEXT]", msg)

    msg_html = MIMEText(email_body, 'html')
    email_msg.attach(msg_html)

    # with open('quotes.png', 'rb') as file:
    #     msg_image = MIMEImage(file.read())
    #
    # msg_image.add_header('Content-ID', '<quote>')
    # email_msg.attach(msg_image)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=addrs,
            msg=email_msg.as_string())


def get_random_quote():
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
        return random.choice(quotes)


now = dt.datetime.now()
if now.weekday() == 4:
    send_email("hugo.andreassa@gmail.com", "Motivational Quotes", get_random_quote())
