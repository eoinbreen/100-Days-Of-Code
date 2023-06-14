import requests
from bs4 import BeautifulSoup

# date = input("What date do you want to travel to? Please type the date in this format YYYY-MM-DD: ")
date = "1992-05-18"
URL = "https://www.billboard.com/charts/hot-100/" + date

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

title_list = [song.getText() for song in soup.select(selector='.o-chart-results-list__item>h3')]
artist_messy_list = [song.getText() for song in soup.findAll(name="span", class_="c-label")]

artist_list = []

for i in range(4, 800, 8):
    artist_list.append(artist_messy_list[i])

print(title_list)
print(artist_list)
