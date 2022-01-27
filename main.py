from bs4 import BeautifulSoup
import requests

response = requests.get(
    url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
top_movies = response.text
soup = BeautifulSoup(top_movies, "html.parser")

films_names = soup.findAll(name="h3", class_="title")
films_list = [name.get_text() + "\n" for name in films_names]
films_list.reverse()

with open("movies_list.txt", "w") as f:
    f.writelines(films_list)