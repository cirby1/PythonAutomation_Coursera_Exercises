#Iterate through the keys and values of a dictionary.
#Return the keys and values in a formatted string using the .format() function. 

My_Game_Message = ""

Game_Collection = {"N64": "Ocarina of Time", "SNES": "A Link to the Past", "Switch": "Breath of the Wild", "Switch2": "Tears of the Kingdom"}

for console, game in Game_Collection.items():
    print("The Console is {} and the best game on the console is {}.".format(console,game))

#Okay, I was able to iterate through the key, value pairs using a for loop and I was able to print a custom message using the data in each key,value pair. 
