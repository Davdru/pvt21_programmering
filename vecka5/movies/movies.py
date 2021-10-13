from rich import print

# Det är en dålig idé att spara känslig data som API-nycklar etc. i kod som är
# Versionshanterad.
from vecka5.movies.omdb_api import MovieNotFound, get_movie_by_title, search_by_title



def print_movie(movie):
    print(f"{movie['Title']} {movie['Year']} regiserad av {movie['Director']}\n")
    print(f"Skådespelare {movie['Actors']} \n")
    print(f"{movie['Plot']}\n")
    print(f"IMDB-betyg: {movie['imdbRating']}")
    print(f"Utmärkelser: {movie['Awards']}")


def get_selection(prompt: str, begin: int, end: int):
    help_text = f"Enter a number between {begin} and {end}"
    while True:
        try:
            res = int(input(prompt))
            if begin <= res <= end:
                return res
            else:
                print(help_text)
        except ValueError:
            print(help_text)


def main():
    # Fråga användaren efter filmtitel och skriv ut data
    # tills användaren matar in ett tomt svar
    while True:
        title = input('Search for title>').strip()
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


            # res['Search'] innehåller en lista av filmer som hittats
            # Första filmen har index 0, andra index 1 osv.
            try:
                selected = get_selection("Select title>", 0, len(res['Search']))
                if selected:
                    t = res['Search'][selected-1]
                    movie_title = t['Title']
                    movie = get_movie_by_title(movie_title)
                    print_movie(movie)
            except IndexError:
                print("Not in list")

        except MovieNotFound as e:
            print(e)





if __name__ == '__main__':
    main()
