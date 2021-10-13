import requests


URL = "http://www.omdbapi.com/"

with open('api_key') as f:
    API_KEY = f.read()


class MovieNotFound(Exception):
    pass


def get_movie_by_title(title: str):
    params = {'t': title, 'apikey': API_KEY}
    res = requests.get(URL, params).json()
    if res['Response'] == 'True':
        return res
    else:
        raise MovieNotFound(f"{title} not found in omdb")


def search_by_title(title: str):
    params = {'s': title, 'apikey': API_KEY}
    res = requests.get(URL, params).json()
    if res['Response'] == 'True':
        return res
    else:
        raise MovieNotFound(res['Error'])