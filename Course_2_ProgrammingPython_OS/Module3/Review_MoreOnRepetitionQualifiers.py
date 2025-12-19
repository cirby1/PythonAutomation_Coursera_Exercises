#Import regular expressions as a module always so we can use the package regular expressions tools. 
#import re

#print(re.search(r"[a-zA-Z]{5}", "a ghost"))
#r "" - means raw string
#[] - filter and select one
#a-zA-Z - any letter upper or lower
#{5} - means times 5.
#So overall it's going to scan and find at least a 5 letter chunk word.

#Import regular expressions as a module so we can use the re tools.
import re
#print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))
#r " " - raw string. 
#[a-zA-Z] - this meeans any letter upper or lower.
#{5} - means times 5
#I believe this will just capture the first instance of the match. So yes, in this case it's 'scary'. 





