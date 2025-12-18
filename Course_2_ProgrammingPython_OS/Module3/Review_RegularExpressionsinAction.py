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
#Step 1: 
