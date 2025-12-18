#If the text passed looks like a standard sentence, meaning that it starts with an uppercase letter, followed by at least some lowercase letters or a space, and ends with a period, question mark, or exclamation point. 
import re

def check_sentence(text):
    result = re.search(r"^[A-Z][a-z\s]*[\.\?\!]$", text)
    print(result)
    return result != None

#print(check_sentence("Is this a sentence?")) #True it has a upppercase at the beginning and it ends with a at least one of those things.
#print(check_sentence("is this a sentence?")) #False it doesn't have a uppercase at the beginning. 
#print(check_sentence("Hello")) #False it doesn't end with one of those characters. 
#print(check_sentence("1-2-3-GO!")) #False, it doesn't start with an alpha character.
print(check_sentence("A star is born.")) #True, it both begins with an uppercase and ends with at least one of those characters.
