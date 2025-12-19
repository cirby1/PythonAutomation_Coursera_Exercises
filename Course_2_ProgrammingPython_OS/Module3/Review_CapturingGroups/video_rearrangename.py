#Fix the regular Expression used in the rearrange function so that it matches middle names, middle initials, as well as double surnames.

import re


print(re.search(r"^([A-Z]\w*),\s([A-Z][\w\.\-]*)\s([A-Z][\w\.\-]*)$",  "Kennedy, John Franklin"))


