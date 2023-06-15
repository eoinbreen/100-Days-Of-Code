import requests
from bs4 import BeautifulSoup

# date = input("What date do you want to travel to? Please type the date in this format YYYY-MM-DD: ")
date = "2023-06-15"
URL = "https://www.billboard.com/charts/hot-100/" + date

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

title_list = [title.getText().strip() for title in soup.select(selector='.o-chart-results-list__item>h3')]
artist_messy_list = [artist.getText() for artist in soup.findAll(name="span", class_="c-label") if artist.getText().strip() != "NEW" and artist.getText().strip() != "RE-\nENTRY"]

artist_list = []

for i in range(4, 800, 8):
    artist_list.append(artist_messy_list[i].strip())

print(title_list)
print(artist_list)

with open(date+" Top 100.txt", mode="w", encoding="utf-8") as file:
    index = 1
    for title in title_list:
        file.write(str(index) + ". " + title + " - " + artist_list[index-1] + "\n")
        index = index + 1
