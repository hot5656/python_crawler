import requests
from bs4 import BeautifulSoup
import lxml


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "lxml")
movies = soup.select("h3.title")

with open("movie100.txt", "w", encoding='utf-8') as file:
    for movie in reversed(movies):
        file.write(f"{movie.text}\n")