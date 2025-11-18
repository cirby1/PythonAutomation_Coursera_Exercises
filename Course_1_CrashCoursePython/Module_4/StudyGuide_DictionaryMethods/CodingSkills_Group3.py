"""
Skills Group 3
-Use the dictionary[key] = value operation to associate a value with a key in a dictionary.
-Iterate over the keys with multiple values from a dictionary, using nested for loops and an if-statement  and the dctionary.items() method.
-Use the dictionary[key].append[value] method to add the ey, a string, and the key for each item in the dictionary.
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


