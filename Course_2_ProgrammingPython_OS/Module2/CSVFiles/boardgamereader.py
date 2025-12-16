import csv

with open("boardgames.csv") as boardgames:  
    boardgamereader = csv.DictReader(boardgames)
    for row in boardgamereader:
        print("{} is a fun game.".format(row["name"]))
