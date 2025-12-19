#This is the same program from before. It gets a name and then writes it out firstname and then last name. Nothing to it...
import re

def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])

print(rearrange_name("Ritchie, Dennis"))





