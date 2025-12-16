import csv

boardgames = [{"name": "villainous", "category": "family", "fun": "very"}, {"name": "CandyLand", "category": "childrens", "fun": "okay"}, { "name": "chess", "category":"strategy", "fun": "average"}]

keys = ["name", "category", "fun"]

with open("boardgame_writer.csv", "w") as boardgame_writer:
    writer = csv.DictWriter(boardgame_writer,fieldnames=keys)
    writer.writeheader()
    writer.writerows(boardgames)


