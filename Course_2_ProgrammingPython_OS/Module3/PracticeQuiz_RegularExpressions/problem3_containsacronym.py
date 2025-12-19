#3 - The contains_acronym() function checks the text for the presence of 2 or more characters or digits surrounded by parenthesis, with at least the first character in uppercase(if it's a letter), returning True if the condition is met, or False otherwise. For example, "Instant messaging (IM) is a set of communication technologies used for text-based communication" should return True since (IM) satisfies the match conditions. Fill in the regular expression in the function.
#Parenthesis with at least 2 or more characters or digits within the parenthesis. With at least the first character being uppercase(if it's a letter)

import re
def contains_acronym(text):
    pattern = r"\([A-Z0-9][\w\d]+\)"
    result = re.search(pattern, text)
    if result != None:
        print(result.group())
        return result

print("SHOULD BE TRUE")
print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print()

print("SHOULD BE TRUE")
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print()

print("SHOULD BE FALSE")
print(contains_acronym("Please do NOT enter without permission!")) # False
print()

print("SHOULD BE TRUE")
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print()

print("SHOULD BE TRUE")
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True
print()





