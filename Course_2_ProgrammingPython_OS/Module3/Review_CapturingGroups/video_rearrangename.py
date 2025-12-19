#Fix the regular Expression used in the rearrange function so that it matches middle names, middle initials, as well as double surnames.

import re
def rearrange_names(name):
    result = re.search(r"^(\w)*, (\w)*$", name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])

name = rearrange_names("Kennedy, John F.")
print(name)

