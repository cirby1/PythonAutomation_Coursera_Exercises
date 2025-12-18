import re

print(re.search(r"\w+\s+\w+", "shopping_list: milk, bread, eggs."))
#print(re.search(r"\w*\s\w*", "123 Ready Set GO"))
#print(re.search(r"\w*\s\w*", "username user_01"))
#print(re.search(r"\w*\s\w*", "shopping_list: milk, bread, eggs."))

#The text passed has to have at least 2 groups of alphanumeric characters (including letters, numbers, and underscores) separated by one or more whitespace characters.


#Okay, so the mistake I made was using * which is lazier and is expressed "nothing or more" while + is expressed one or more. That's why some hits were going through because some parts were just finding nothing. And the rest was picking everything else up.




"""
import re
def check_character_groups(text):
    result = re.search(r"", text)
    return result != None
print(check_character_groups("One")) #False
"""
