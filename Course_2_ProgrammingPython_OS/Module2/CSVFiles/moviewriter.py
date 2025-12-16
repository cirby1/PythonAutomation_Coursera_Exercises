import csv

movies = [{"name": "titanic", "company": "universal", "revenue": 400}, {"name": "avatar", "company": "amc", "revenue": 300}, {"name": "jaws", "company": "universal", "revenue": 200}]

keys = ["name", "company", "revenue"]

with open("movie_writer.csv", "w") as movie_writer:
    writer = csv.DictWriter(movie_writer, fieldnames=keys)
    writer.writeheader()
    writer.writerows(movies)

