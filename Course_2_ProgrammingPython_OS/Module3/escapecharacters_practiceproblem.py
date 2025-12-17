#Fill in the code to check if the text passed has at least 2 groups of alphanumeric characters (including letters, numbers, and underscores) separated by one or more whitespace characters.

#import re
print(re.search(r"\w*\s*\w*", "username user_01"))

import re
def check_character_groups(text):
    result = re.search(r"\w+\s", text)
    return result != None

#So I need to see if the text passed has at least two groups of alphanumeric chracters (letters, numbers, and underscores) separated by one or more whitespace characters.

#I think I will have to use the w thing so I would need to escape it twice? Maybe \w\w?

print(check_character_groups("One")) #False

print(check_character_groups("123 Ready Set Go")) #True

print(check_character_groups("username user_01")) #True

print(check_character_groups("shopping_list: milk, bread, eggs")) #False
