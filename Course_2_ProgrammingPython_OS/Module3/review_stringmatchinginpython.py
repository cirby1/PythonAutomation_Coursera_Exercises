#Here is just a follow a long of different examples of using regex. Seems pretty easy to me, now that I kind of understand the structure.

"""
#Here we are searching for the regex "aza" in the string "plaza". Don't forget to make the regex expressions just raw strings using r" ".
import re
result = re.search(r"aza", "plaza")
print(result)
#We get a match obviously
"""

"""
import re
result = re.search(r"aza", "bazaar")
print(result)
#We get a match.
"""

"""
import re
result = re.search(r"aza", "maze")
print(result)
print(re.search(r"^x", "xenon"))
#We get a match and the object tells us where in the regex. It uses string number or indexing.
"""

"""
import re
print(re.search(r"p.ng", "penguin"))
#We get a match at index 0 through 4. Remember it's up to, but not including 4. 
"""

"""
import re
print(re.search(r"p.ng", "clapping"))
print(re.search(r"p.ng", "sponge"))
#We get a match at index 1 to 5. 
"""

"""
import re
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))
#Match at index 0 to 4.
"""

















