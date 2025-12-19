#Fix the regular Expression used in the rearrange function so that it matches middle names, middle initials, as well as double surnames.

#import re
#This line finally works! I was able to get it to be accepted by the video exercise.
#print(re.search(r"^([A-Z]\w*),\s([A-Z][\w\.\-]*)\s?([A-Z][\w\.\-]*)$",  "Kennedy, John-F."))

import re
def rearrange_name(name):
    result = re.search(r"([A-Z]\w*),\s([A-Z][\w\.\-]*)\s?([A-Z][\w\.\-]*)$", name)
    if result == None:

name=rearrange_name("Kennedy, John F")
print(name)


