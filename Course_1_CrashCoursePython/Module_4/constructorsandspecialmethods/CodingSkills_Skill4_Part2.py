"""
Create a copy of a dictionary.
Iterate through the values of the new dictionary.
Change each value in the new dictionary, while keeping the same keys.
"""

Game_Collection = {"N64": "Ocarina", "Gamecube": "Windwaker", "Switch":"Breath of the Wild"}

Sold_Collection = Game_Collection.copy()

for console, game in Sold_Collection.items():
    print(console, game)

print("Wait! Each Game is broken!!! Let's update the status and print it again!")

for console, game in Sold_Collection.items():
    Sold_Collection[console] = "Broken" + " " + game

print(Sold_Collection.items())

#Okay, I think I did a good job of updating each one. Good!!!!
