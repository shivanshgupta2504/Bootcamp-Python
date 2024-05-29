import smtplib
import datetime as dt
import random

my_email = "shivanshsg25@gmail.com"
password = "sclasnrncresyzvr"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:  # Monday
    with open("quotes.txt") as file:
        quotes = file.readlines()
        quote = random.choice(quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )


