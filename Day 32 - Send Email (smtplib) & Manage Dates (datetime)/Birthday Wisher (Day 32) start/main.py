import smtplib

my_email = "eoinbreen185@gmail.com"
password = "vtdpykloradcdwxv"
recipient = "eoinbreen185@yahoo.com"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=recipient,
        msg="Subject:Hello\n\nThis is the body of my email"
    )
