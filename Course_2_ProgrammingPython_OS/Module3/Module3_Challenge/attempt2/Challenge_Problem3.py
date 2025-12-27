import re

def secure_website(str_website_input):
    regex = r"^\w{5}://(www\.)(\w+)(\.\w+)$"
    result = re.search(regex, str_website_input)
    if result is None:
        return "not"
    return result.group(2)

print(secure_website("http://www.text.com"))
print(secure_website("https://www.text.com"))
print(secure_website("http://www.text.co"))
print(secure_website("https://www.text.co"))

#Okay, well my output was correct. Let's see what happens...




