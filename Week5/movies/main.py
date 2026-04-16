import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

def fetch_movies():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    movies = soup.find_all("h3", class_="title")
    return [m.get_text() for m in movies][::-1]