import re

with open("pb_texts.txt", "r") as file:
    book_content = file.read()

match = re.search(r'"[^"]*!"', book_content)

if match:
    print("Found it: ", match.group())


