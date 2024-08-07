import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
soup = BeautifulSoup(response.text, "html.parser")

movie_tags = soup.select(selector="h3.title")
movie_titles = [movie.getText() for movie in movie_tags]
movie_titles = movie_titles[::-1]

with open("100Movies.txt", "w", encoding="utf-8") as file:
    for i in range(len(movie_titles)):
        file.write(f"{movie_titles[i]}\n")




