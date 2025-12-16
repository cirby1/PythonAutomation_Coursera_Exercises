import csv

with open("movies.csv") as movies:
    movie_reader = csv.DictReader(movies)
    for row in movie_reader:
        print("The movie {} is owned by {} and has made {} million dollars.".format(row["name"], row["company"], row["revenue"]))
