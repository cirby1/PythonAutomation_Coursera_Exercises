#1. The check web address function checks if the text passed qualifies as a top level web address, meaning it contains alphanumeric characters (which include letters, numbers, and underscores), as well as periods, dashes, and a plus sign, followed by a period and a character-only top level domain such as ".com", ".info", ".edu", etc. Fill in the regular expression to do that, using escape characters. 

import re
def check_web_address(text):
    pattern = r"[/w/d_*][\.\-\+]\.[\w*]"
    result = re.search(pattern, text)
    return result != None

print(check_web_address("gmail.com")) #True

print(re.search(r'[a-zA-Z0-9_]*.[a-z]*$', 'gmail.com'))
