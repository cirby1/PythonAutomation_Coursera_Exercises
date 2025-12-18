#import re
#print(re.search(r"A.*a", "Argentina"))
#I interpret this as saying find Capital A plus any character chunk and up to an a. But since it's greedy it will keep going all the way until it finds the last a.
#print(re.search(r"A.*a", "Azerbaijan")) #It's the same thing here.
#print(re.search(r"^A.*a$", "Australia")) #It's the same thing here. 

import re
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
#Looking at the beginning, I'm thinking this is sayingany alphabetical character a-z lower or upper or an underscore, any alphas followed by underscores, lazy matching until the end.
#print(re.search(pattern, "_this_is_a_valid_variable_name"))

print(re.search(pattern, "this isn't a valid variable name"))

#So that pattern is saying.
#First make sure the match starts at the beginning of the line. ^
#[a-zA-Z_] match exactly one character that is alpha or underscore. AND NOT A NUMBER. ELIMINATING ANY NUMBERS TO START THE STRING. Okay, this makes sense.
#Do it again. Match exactly one [a-zA-Z0-9_]

#Okay in a bit let's break it down with AI in plain English.
#Step 1: Start of the String - ^ - Ensures the match begins with the very first character.

#Step 2: The First Character - [a-zA-Z_] - So the first character can be an alphabetical character upper or lower, or an underscore. This ensures the first character of say a username isn't a number or some other obscure character.

#Step 3: The following characters - [a-zA-Z0-9_] - So the following characters can be a through z upper or lower, numbers, or underscore. 

#Step 4: * Means Zero or more for the preceding group. So it's gonna be a big clump of characters. 

#Step 5: $ Means make sure it goes all the way to the end without trailing characters. It means the end of the input string. Or however long it is. 

#So overall it means look for a clump of text. The first character is limited and the rest isn't so limited. It's more like a username finder. And it will only have underscores between words. 
