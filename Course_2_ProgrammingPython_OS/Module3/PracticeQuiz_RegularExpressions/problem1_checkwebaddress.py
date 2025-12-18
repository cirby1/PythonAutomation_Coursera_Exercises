#1. The check web address function checks if the text passed qualifies as a top level web address, meaning it contains alphanumeric characters (which include letters, numbers, and underscores), as well as periods, dashes, and a plus sign, followed by a period and a character-only top level domain such as ".com", ".info", ".edu", etc. Fill in the regular expression to do that, using escape characters. 



import re
def check_web_address(text):
    #pattern = r"^\w*[\.\-\_][a-z]*"
    pattern = r"^(www\.)?\w*"
    result = re.search(pattern, text)
    print(result)
    return result != None

print("gmail.com - SHOULD BE TRUE")
print(check_web_address("gmail.com")) #True
print()

print("www@google")
print(check_web_address("www@google")) #True
print()

print("www.Coursera.com")
print(check_web_address("www.Coursera.com")) #True
print()

print("web-address.com/homepage")
print(check_web_address("web-address.com/homepage")) #True
print()

print("My_Favorite-Blog.US")
print(check_web_address("My_Favorite-Blog.US")) #True
print()

#import re
#print(re.search(r'[a-zA-Z0-9_]*(\.?).[a-z]*$', 'gmail.com'))
#print(re.search(r'^\w*\.\w*.\w*$', 'web-address.com/homepage'))
#print(re.search(r'^[a-zA-Z0-9_\.\-\+]*(\.)?.[a-z]*$', 'www@google'))
