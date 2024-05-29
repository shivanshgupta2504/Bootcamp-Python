import smtplib

my_email = "shivanshsg25@gmail.com"
password = "sclasnrncresyzvr"

# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs="shivanshgupta2057@gmail.com",
#     msg="Subject:Hello\n\nThis is body of my email."
# )
# connection.close()

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="shivanshgupta2057@gmail.com",
        msg="Subject:Hello\n\nThis is body of my email."
    )
