#You are reading an article that includes some government websites in the form:

#https://www.website-domain.gov

#You would like a list of these websites by extracting them from the text automatically, instead of copying and pasting them by hand. Complete the function find_gov_urls() to accomplish this task for all websites that end with .gov.

import re

def find_gov_urls(website):
    pattern = r"https://www\.[\w\-]+\.[\w]+"
    result = re.findall(pattern,website)
    return result

print(find_gov_urls("https://www.data.gov is a great open source website. And so is https://www.nsacracker.gov"))





