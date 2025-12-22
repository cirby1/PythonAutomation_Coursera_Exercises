#When capturing regex groups, what datatype does the groups method return?
#A String
#B A Tuple
#C A List
#D A float

import re

regex = r"(\w{4})"

result = re.search(regex, "once upons")
print(result.groups())
print(type(result))

#When I run the function it returns a tuple.

