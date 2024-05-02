import schedule
import time
import random
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

QUOTES = [
    "Hanya ada satu cara untuk melakukan pekerjaan besar, yaitu dengan mencintai apa yang Anda lakukan. - Steve Jobs",
    "Pada akhirnya, kita hanya akan mengingat bukan kata-kata dari musuh kita, tetapi keheningan dari teman-teman kita. - Martin Luther King Jr.",
    "Keberhasilan bukanlah sesuatu yang final, kegagalan bukanlah sesuatu yang fatal: Yang penting adalah keberanian untuk terus maju. - Winston Churchill",
    "Percaya bahwa Anda bisa dan Anda sudah setengah jalan menuju kesuksesan. - Theodore Roosevelt",
    "Keagungan terbesar dalam hidup bukanlah tidak pernah jatuh, tetapi dalam bangkit setiap kali kita jatuh. - Nelson Mandela"
]

EMAIL_PENGGUNA = os.environ['EMAIL_PENGGUNA']
SANDI_EMAIL = os.environ['SANDI_EMAIL']

def send_email():
    email = "Jangan lupa untuk istirahat sejenak!"
    server = "smtp.gmail.com"
    port = 587
    s = smtplib.SMTP(host=server, port=port)
    s.starttls()
    s.login(EMAIL_PENGGUNA, SANDI_EMAIL)

    msg = MIMEMultipart()
    msg['To'] = 'contoh@gmail.com'  # Ganti dengan alamat email tujuan
    msg['From'] = EMAIL_PENGGUNA
    msg['Subject'] = "Kutipan untuk hari ini"
    msg['Body'] = QUOTES[random.randint(0, 4)]
    msg.attach(MIMEText(email, 'html'))

    s.send_message(msg)
    del msg
    s.quit()

def display_log():
    print("sended random quote")
    send_email()

schedule.every(1).hours.do(display_log)

while True:
    schedule.run_pending()
    time.sleep(1)