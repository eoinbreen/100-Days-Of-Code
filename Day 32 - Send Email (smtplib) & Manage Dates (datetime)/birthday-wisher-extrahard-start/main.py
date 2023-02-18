##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
data = pandas.read_csv("birthdays.csv")
records = data.to_dict(orient="records")

my_email = "eoinbreen185@gmail.com"
password = "vtdpykloradcdwxv"

now = dt.datetime.now()
for record in records:
    if now.day == record["day"] and now.month == record["month"]:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        letter_num = random.randint(1, 3)
        with open(f"letter_templates/letter_{letter_num}.txt", mode="r") as file:
            letter = file.read()
        letter = letter.replace("[NAME]", record["name"])
        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=record["email"],
                msg=f"Subject:Happy Birthday\n\n{letter}"
            )








