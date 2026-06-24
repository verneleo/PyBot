import requests
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("X-API-KEY")

resp = os.getenv("REQ")

headers = { "X-API-KEY" : TOKEN }


URL = "https://api.poiskkino.dev/v1.4/movie/random"
def get_random_movie(genre):

    params = {
        "notNullFields" : ["name",
                            "description",
                            "year",
                            "rating.kp",
                            "poster.url"
        ],
        "type" : "movie",
        "year" : "1990-2026",
        "rating.kp" : "7.4-10",
        "countries.name": ["США", "Великобритания", "Россия"],
        "votes.kp" : "100000-9999999",
        "top-250" : "1-200",
        "genres.name" : genre
    }

    response = requests.get(URL, params=params, headers=headers)

    docs = response.json()

    name = docs['name']

    year = docs['year']

    rate = docs['rating']['kp']

    desc = docs['description']

    country = docs['countries'][0]['name']

    movieLenght = docs['movieLength']

    poster_url = docs['poster']['url']

    return year, name, rate, desc, poster_url, movieLenght, country
