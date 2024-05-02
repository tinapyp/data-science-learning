import requests
import smtplib
import os
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from replit import db
import schedule
import time

EMAIL_PENGGUNA = os.environ["EMAIL_PENGGUNA"]
SANDI_EMAIL = os.environ["SANDI_EMAIL"]


def get_price():
    date = datetime.date.today()
    URL = "https://www.tokopedia.com/atrinitykomputer/macbook-air-m2-2022-13-inch-ram-16gb-256gb-512gb-1tb-ssd-midnight-inter-10core-16gb-1tb-3e2b7"
    response = requests.get(URL).text
    soup = BeautifulSoup(response, "html.parser")
    price = soup.find("div", {"class": "price"}).text.strip()

    db["macbook"] = {"time": date, "price": price}

    return price


def send_email():
    server = "smtp.gmail.com"
    port = 587
    s = smtplib.SMTP(host=server, port=port)
    s.starttls()
    s.login(EMAIL_PENGGUNA, SANDI_EMAIL)

    msg = MIMEMultipart()
    msg["To"] = "contoh@gmail.com"
    msg["From"] = EMAIL_PENGGUNA
    msg["Subject"] = "Harga Turun oik"
    msg.attach(MIMEText("Harga Macbook turun! Cek sekarang.", "plain"))

    s.send_message(msg)
    del msg
    s.quit()


def check_price():
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    yesterday_price = float(
        db["macbook"]
        .get(yesterday)["price"]
        .replace("Rp", "")
        .replace(".", "")
        .replace(",", ".")
    )
    today_price = float(
        get_price().replace("Rp", "").replace(".", "").replace(",", ".")
    )
    if yesterday_price > today_price:
        return True


def main():
    send = check_price()
    if send:
        send_email()


schedule.every(8).hours.do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
