import smtplib
import datetime as dt
import random


my_email = "eoinbreen185@gmail.com"
password = "vtdpykloradcdwxv"
recipient = "eoinbreen185@yahoo.com"

now = dt.datetime.now()
day = now.weekday()
if day == 0:
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
    quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )







