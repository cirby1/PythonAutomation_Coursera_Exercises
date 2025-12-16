import csv

games = [{"name": "NES", "company": "Nintendo", "units": 350}, {"name": "Xbox", "company": "Microsoft", "units": 250}, {"name": "Playstation", "company": "Sony", "units": 599}]

keys = ["name", "company", "units"]

with open("games_writer.py", "w") as game_writer:
    game_writer = csv.DictWriter(game_writer,fieldnames=keys)
    game_writer.writeheader()
    game_writer.writerows(games)
