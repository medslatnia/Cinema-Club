import os
import json
import logging

CURR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CURR_DIR, "data", "movies.json")

def get_movies():
    with open (DATA_FILE, "r") as f:
        movies_title = json.load(f)

        movies = [Movie(movie_title) for movie_title in movies_title]
        return movies


class Movie():
    def __init__(self, title):
        self.title = title.title()

    def __str__(self):
        return self.title

    def _get_movies(self):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
            


    def _write_movies(self, movies):
        with open(DATA_FILE, 'w') as f:
            json.dump(movies, f, indent=4)

    def add_to_movies(self):
        #get the list of movies
        movies = self._get_movies()
        #check that the movie is not already in the list
        if self.title not in movies:
            #if not, we add it
            movies.append(self.title)
            self._write_movies(movies)
            return True

        else:
            #if yes, write a logging message
            logging.warning(f"the film {self.title} is already on the list. ")

    def remove_from_movies(self):
        #get list of movies
        movies = self._get_movies()
        #check if the film is on the list
        if self.title in movies:
        #if yes, remove it. Then write the new list on json file
            movies.remove(self.title)
            self._write_movies(movies)


if __name__ == "__main__":
    movies = get_movies()
    print(movies)
