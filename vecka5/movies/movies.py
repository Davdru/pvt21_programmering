import requests

URL = "http://www.omdbapi.com/"
# Det är en dålig idé att spara känslig data som API-nycklar etc. i kod som är
# Versionshanterad.
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


def main():
    # Fråga användaren efter filmtitel och skriv ut data
    # tills användaren matar in ett tomt svar
    while True:
        title = input('Title>').strip()
        if title == "":
            break

        try:
            res = search_by_title(title)
            # Använd requests.get() för att hämta data om en film från omdbapi
            # if res['Response']
            # print_movie(res)

            # [1] Alien (1979)
            # [2] Alien3 (1992)
            for i, m in enumerate(res['Search'], start=1):
                print(f"[{i}] {m['Title']} ({m['Year']})")

            selected = int(input(">"))
            t = res['Search'][selected-1]
            print(t)

        except MovieNotFound as e:
            print(e)


def print_movie(movie):
    print(f"{movie['Title']} {movie['Year']} regiserad av {movie['Director']}\n")
    print(f"Skådespelare {movie['Actors']} \n")
    print(f"{movie['Plot']}\n")
    print(f"IMDB-betyg: {movie['imdbRating']}")
    print(f"Utmärkelser: {movie['Awards']}")


if __name__ == '__main__':
    main()
