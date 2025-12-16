import csv

with open("games.csv") as games:
    reader = csv.DictReader(games)
    for row in reader:
        print("{} has {} amount of games sold.".format(row["name"], row["units"]))   
