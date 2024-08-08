import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()

# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
#     "Accept-Encoding": "gzip, deflate, br, zstd",
#     "Accept-Language": "en-US,en",
#     "Priority": "u=0, i",
#     "Sec-Ch-Ua": '"Not)A;Brand";v="99", "Brave";v="127", "Chromium";v="127"',
#     "Sec-Ch-Ua-Mobile": "?0",
#     "Sec-Ch-Ua-Platform": '"Windows"',
#     "Sec-Fetch-Dest": "document",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-Site": "cross-site",
#     "Sec-Fetch-User": "?1",
#     "Sec-Gpc": "1",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 "
#                   "Safari/537.36",
# }

headers = {
    "Accept-Language": "en-US,en",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 "
                  "Safari/537.36",
}

my_email = os.getenv("EMAIL_ADDRESS")
my_password = os.getenv("EMAIL_PASSWORD")
my_smtp_address = os.getenv("SMTP_ADDRESS")

response = requests.get(url="https://www.amazon.in/Juarez-Acoustic-Cutaway-038C-Strings/dp/B017NPCSLI/ref=sr_1_5?sr=8-5"
                        , headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())

target_price = 7000

price_tag = soup.find(name="span", class_="a-offscreen")
print(price_tag)
product_title_tag = soup.find(name="span", id="productTitle")
print(product_title_tag)
product_title = product_title_tag.getText().strip()
price = float(price_tag.getText().split("$")[1])

if price < target_price:
    message = f"{product_title} is now {price}\n https://appbrewery.github.io/instant_pot/".encode("UTF-8")
    with smtplib.SMTP(my_smtp_address, port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="shivanshgupta2057@gmail.com",
            msg=message,
        )
