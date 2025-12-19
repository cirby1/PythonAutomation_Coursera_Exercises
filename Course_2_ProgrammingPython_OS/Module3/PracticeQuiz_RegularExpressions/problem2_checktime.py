#2 - The check_time() function checks for the time format of a 12 hour clock. Functions are like vending machines. as follows: the hour is between 1 and 12, with no leading zero, followed by a colon, then minutes between 00 and 59, then an optional space, and then AM and PM, in upper or lowercase. Fill in the regular expression to do that. How many of the concepts that you just learned can you use here?

import re
def check_time(text):
    pattern = r"^[0-9]*:[00-59]+\s?[aApP][mM]$"
    result = re.search(pattern, text)
    print(result)
    return result != None


print("12:45pm - SHOULD BE TRUE")
print(check_time("12:45pm")) #True
print()


print("9:59 AM - SHOULD BE TRUE")
print(check_time("9:59 AM")) #True
print("")

print("6:60am - SHOULD BE FALSE")
print(check_time("6:60am")) #False
print("")

print("five o' clock - SHOULD BE FALSE")
print(check_time("five o' clock")) #False
print("")

print("6:02 am - SHOULD BE TRUE")
print(check_time("6:02 am")) #True
print("")

print("6:02km - SHOULD BE FALSE")
print(check_time("6:02km")) #False
print("")







