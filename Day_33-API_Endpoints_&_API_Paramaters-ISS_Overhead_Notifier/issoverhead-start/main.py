import requests
from datetime import datetime
import smtplib
import time


MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

MY_EMAIL = "e.breen185@gmail.com"
password = "vtdpykloradcdwxv"
recipient = "eoinbreen185@yahoo.com"


# Your position is within +5 or -5 degrees of the ISS position.
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    margin = 5
    if MY_LAT + margin >= iss_latitude >= MY_LAT - margin and MY_LONG + margin >= iss_longitude >= MY_LONG - margin:
        return True
    return False


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour = time_now.hour
    if hour <= sunrise or hour >= sunset:
        return True
    return False


def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=password)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:ISS in View\n\nLook Up"
        )


while True:
    time.sleep(60)
    if is_iss_overhead() and is_dark():
        send_email()

