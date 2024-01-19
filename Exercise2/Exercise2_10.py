# File name:    Exercise2_10.py
# Author:       Eerik Vainio
# Description:  

class Movie:
    def __init__(self, name: str, director: str, genre: str, year: int):
        self.name = name
        self.director = director
        self.genre = genre
        self.year = year

# Return a new list which only includes movies that have the given genre
def movies_of_genre(movies: list, genre: str):
    new_list = []
    for x in movies:
        if(x.genre == genre):
            new_list.append(x)
    
    return(new_list)


john_woo = Movie("A Better Tomorrow", "John Woo", "action", 1986)
kungfu = Movie("Chinese Odyssey", "Stephen Chow", "comedy", 1993)
jet_li = Movie("The Legend", "Corey Yuen", "comedy", 1993)

movies = [john_woo, kungfu, jet_li, Movie("Hero", "Yimou Zhang", "action", 2002)]

print("Movies in the action genre:")
for movie in movies_of_genre(movies, "action"):
    print(f'{movie.director}: {movie.name}')