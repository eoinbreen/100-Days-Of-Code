import requests
from bs4 import BeautifulSoup

URL="https://www.amazon.co.uk/Samsung-Galaxy-Android-Smartphone-Phantom/dp/B09NRRVPZ7/ref=sr_1_3?crid=2JF3OKZJBLW8C&keywords=samsung+galaxy+s22&qid=1687206141&sprefix=samsung+galaxy+s22%2Caps%2C77&sr=8-3"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
}

response = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

price = soup.find(name="span", class_="a-offscreen").getText()
price = float(price.split("£")[1])


print(price)

