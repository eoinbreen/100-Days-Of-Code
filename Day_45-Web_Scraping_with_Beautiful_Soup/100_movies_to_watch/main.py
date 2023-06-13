import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

movie_list = [movie.getText() for movie in soup.findAll(name="h3", class_="title")]

movie_list.reverse()


with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movie_list:
        file.write(movie + "\n")

