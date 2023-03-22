from flight_data import FlightData
import os
import smtplib

MY_EMAIL = "eoinbreen185@yahoo.com"
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
RECIPIENT = "eoinbreen185@yahoo.com"

class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, flight: FlightData):
        self.flight = flight

    def send_notification(self):
        message = f"Low Price Alert! Only {self.flight.price} Euros to fly from " \
                  f"{self.flight.origin_city} - {self.flight.origin_airport} to " \
                  f"{self.flight.destination_city} - {self.flight.destination_airport} from " \
                  f"{self.flight.out_date} to {self.flight.return_date}"

        if self.flight.stop_overs > 0:
            message += f"\nFlight has {self.flight.stop_overs} stop over, via {self.flight.via_city}."
            print(message)
        print(message)
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=RECIPIENT,
                msg=f"Flight Deal\n\n {message}"
            )
