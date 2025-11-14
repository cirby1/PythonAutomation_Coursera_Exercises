"""
In this dictionary segment:
    -Properties of the Dictionary Data Type.
    -How Dictionaries differ from Lists. 
    -How to iterate over the contents of a dictionary.
    -How to use dictionaries with lists and strings. 
"""

#Dictionaries are used to organizes ELEMENTS into COLLECTIONS. Dictionaries include key and value pairs. Dictionaries include one or more keys, with one or more values associated with each key.
#Please uncomment or take out the "#" hash tag signs and run the lines of code to see what they do. 
#my_dictionary = {"keyA":["value1", "value2"], "keyB":["value3", "value4"]}
#print(my_dictionary)


#--------------------------------OPERATTIONS FOR DICTIONARIES----------------------------------------------------------------
#There's a bunch of operations one can do with dictionaries.
#Prints the length of the dictionary. Good for figuring out how big it is.
#print(len(my_dictionary)) #Prints the length of the dictionary. I believe starting at #1, then #2, etc...

#This one iterates or goes through each key, great if you need to look for or do some kind of work on each key in the dictionary.
#for key in my_dictionary:
#    print(key)

#This one iterates over every key,value pair in the dictionary.
#for key,value in my_dictionary.items():
#    print(key, value)

#This checks if there is a key in the dictionary. Good to see if something even exists or is even there.
#if "keyA"  in my_dictionary:
#    print("Hey the key exists in here!!! Haha!")

#If you want to access a value, then you just have to put what key to fetch or take the value from.
#print(my_dictionary["keyA"])

#Now, if you want to CHANGE a value you can do this by using the assignment operator or the equals sign "=". You do it like this.
#my_dictionary["keyA"] = ["newstuff", "oldstuff"]
#And if I print the dictionary I will see the changes.
#print(my_dictionary)

#This one supposedly deletes a value from a dictionary by using where it is using it's key.
#del my_dictionary["keyA"]
#It should mean that the first key has an empty value.
#print(my_dictionary)
#If you print the above line only the second key exists now. Since the value got deleted from the first key, both the value and the key vanished, since it no longer had a value.

#---------------------------METHODS FOR DICTIONARIES-------------------------------------------
my_dictionary = {"keyA":["value1", "value2"], "keyB":["value3", "value4"]}

#The Get command will go out and "get" the values at the key address.
#print(my_dictionary.get("keyA"))

#I'm guess this just prints all the keys inside of the dictionary.
#print(my_dictionary.keys())

#The same thing is for the values inside of the dictionary.
#print(my_dictionary.values())

#The append value commands will append a value to an existing key. More like a "stick this here" type of command.
#print(my_dictionary["keyA"].append(["stuff1", "stuff2"]))
#print(my_dictionary)
#This definitely works, but it appends a new value to the end of the list inside of the first value spot of the key specified.
#print(my_dictionary)
#print(my_dictionary["keyA"].append("stuff2"))
#print(my_dictionary)


#The update method will update keys in an existing dictionary by looking at another dictionary. If the same key names are in the other dictionary then the values of the existing keys will just update with their values. 
#my_new_dictionary = {"keyA":["stuff1"], "keyB":["Stuff2"]}
#print(my_dictionary.update(my_new_dictionary))
#print(my_dictionary)

#This nukes the dictionary and clears everything up. 
#my_dictionary.clear()
#print(my_dictionary)

#This copy method is I'm assuming copies the dictionary. 
#my_new_new_dictionary = {}
#print(my_new_new_dictionary)
#my_new_new_dictionary = my_dictionary.copy()
#print(my_new_new_dictionary)

#----------------------------DICTIONARIES VERSUS LISTS------------------------------------------------------
"""
Okay, heres the run down. The dealio. The real dealzzzzzz. Dictionaries and Lists are different. But they got some same things going on.

Both dictionaries and Lists:
    -organize elements into collections.
    -Have to be initialized with an empty form first. Curly braces for dictionaries, and square brackets for lists.
    -Can iterate or cycle through the items or elements in a collection. 
    -Have a toolkit of methods to change the collections. Like removing or adding new stuff.

Dictionaries have the following characteristics:
    -they are unordered.
    -the keys can be any data type.
    -can access values using the keys (duh)
    -can use square brackets inside curleys. I guess lists within a dictionary?
    -YOU HAVE to put a colon between the key and the value. LIke this --->   key: value
    -Use commas to separate key groups and each value within a group.
    -Are quicker than lists. 
"""

#Heres a pet dictionary example. A lil mini example. A little tiny lil guy. 
#pet_dictionary = {"dogs": ["Bella", "George", "Tinkerbell"], "cats": ["Regina", "Orvy", "Molki"]}
#print(pet_dictionary)

#This prints the values at the key "dogs" which is the first spot. Nothing too crazy. 
#print(pet_dictionary.get("dogs", 0))

"""
List only:
    -are unordered, you can put them however you want. I don't think they are in alpha or any sort of scheme.
    -You can access each stuff or thing in a list by it's address or index. It's weird though because the first stuff is number at number 0, then it's 1, then 2, then 3, etc...
    -The indexes are always numbers you won't see them labeling each spot with a letter or some other symbol.
    -Gotta use square brackets. Kind of reminds me of a piece of square paper like a list. 
    -Use commas to separate each list element. 
"""

#Here's another list example















