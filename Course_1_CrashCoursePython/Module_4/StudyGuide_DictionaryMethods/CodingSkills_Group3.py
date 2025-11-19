"""
Skills Group 3
-Use the dictionary[key] = value operation to associate a value with a key in a dictionary.
-Iterate over the keys with multiple values from a dictionary, using nested for loops and an if-statement  and the dctionary.items() method.
-Use the dictionary[key].append[value] method to add the key, a string, and the key for each item in the dictionary.
"""

"""
This function receives a dictionary, which contains resource categories (keys) with a list of available resources (values) for a company's IT department. The resources belong to multiple categoies. The function should reverse the keys and values to show which categories (values) each resource (key) belong to.
"""

"""
This program compares the values in all the other keys, and sees whether there are any matches in them. It will just give a ending list of the part and what lists it shows up in. That's it. So you will need to look at value and check all the other keys and see if it shows up in those keys.
"""

#The dictionary is kind of hard to read, but I can format so that it's easier. 

computer_parts = {

        "desktop": ["monitor", "keyboard", "mouse"],
        "laptop": ["screen", "keyboard", "trackpad"], 
        "console": ["controller", "mouse", "keyboard", "headset", "monitor"],
        "phone": ["earbuds", "battery", "screen"],
}

#Okay, I have some data now. So it needs to return the parts and which categories that they show up in. That's it. 

#First I need to make a master list of just parts.
all_parts_list = []
for technology, parts in computer_parts.items():
    for part in parts:
        if part not in all_parts_list:
            all_parts_list.append(part)

print(all_parts_list)

#Now that I have the parts list I need to find a way to create a dictionary with just keys. And then be able to add the values to the dictionary as I am searching through the entire list. 

parts_location_catalogue = {}

for individual_part in all_parts_list:
    parts_location_catalogue[individual_part] = []

print(parts_location_catalogue)

#Okay now I have the master list of parts. And I have the parts dictionary. I need to iterate through the entire inventory and see if that part is in that list, if it is, then I will add that technology to the list of values for that part. 

for technology, parts in computer_parts.items():
    for part in parts:
        if part in all_parts_list:
            parts_location_catalogue[part].append(technology)

print(parts_location_catalogue)

"""
for technology, parts in computer_parts.items():
    print(technology)
    for part in parts:
        print(part)
    print()
"""

#Okay! I think it worked and I'm really happy with the results!!! Woohoo!!!!!!!!!!!!!
