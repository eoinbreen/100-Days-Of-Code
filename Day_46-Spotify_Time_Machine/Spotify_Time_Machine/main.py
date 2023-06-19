import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os


# Spotipy Documentation - https://spotipy.readthedocs.io/en/2.22.1/

APP_CLIENT_ID = os.environ.get("APP_CLIENT_ID")
APP_CLIENT_SECRET = os.environ.get("APP_CLIENT_SECRET")
REDIRECT_URI = "http://example.com"

auth_manager = SpotifyOAuth(client_id=APP_CLIENT_ID,
                            client_secret=APP_CLIENT_SECRET,
                            redirect_uri=REDIRECT_URI,
                            scope="playlist-modify-private",
                            show_dialog=True,
                            cache_path="token.txt"
                            )

sp = spotipy.Spotify(auth_manager=auth_manager)

user_id = sp.current_user()["id"]

date = input("What date do you want to travel to? Please type the date in this format YYYY-MM-DD: ")

URL = "https://www.billboard.com/charts/hot-100/" + date

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

# Scrape the titles and artists of the top 100 of the inputted date
title_list = [title.getText().strip() for title in soup.select(selector='.o-chart-results-list__item>h3')]
artist_messy_list = [artist.getText() for artist in soup.findAll(name="span", class_="c-label")
                     if artist.getText().strip() != "NEW" and artist.getText().strip() != "RE-\nENTRY"]

artist_list = []

# Clean up the artists list
for i in range(4, 800, 8):
    artist_list.append(artist_messy_list[i].strip())

playlist_name = date+" Billboard 100"

# Creating a text file with the top 100 songs and their artists
with open(f"{playlist_name}.txt", mode="w", encoding="utf-8") as file:
    index = 1
    for title in title_list:
        file.write(str(index) + ". " + title + " - " + artist_list[index-1] + "\n")
        index = index + 1


year = date.split("-")[0]
song_uris = []

# Try to find each song in spotify, throw an exception if it's not on spotify
for song in title_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped")

playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

print(song_uris)
