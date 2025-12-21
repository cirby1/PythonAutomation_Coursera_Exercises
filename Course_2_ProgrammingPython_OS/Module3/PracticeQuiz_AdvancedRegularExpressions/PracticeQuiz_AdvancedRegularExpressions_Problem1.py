#1 - You're working on a CSV File that contains employee information. Each record has a name field, followed by a phone number field, and a role field. The phone number field contains U.S. phone numbers and needs to be modified to the international format, with +1- in front of the phone number. The rest of the phone number should not change. Fill in the regular expressions, using groups, to use the transform_record() function to do that.

import re

def transform_record(record):
    new_record = re.sub(r"(\d{3})-(\d{3})-?(\d{4})", r"+1-\1-\2-\3", record)
    return new_record


#print(transform_record("Sabrina Green, 802-867-5309, IT whatever"))
#print(transform_record("Juan Juano, 999-888-777, CS guy"))
print(transform_record("Peter Paker, 444-443-2232, Spiderman"))



"""

#r"(\d{3})-(\d{3})-(\d{4})"
#blah blah blah
#new_record = re.sub(r"(\d{3})-(\d{3})-(\d{4})", r"+1-\1-\2-\3", "Sabrina Green,802-867-5309,System Administrator")
#print(new_record)
#print(transform_record("Sabrina Green,802-867-5309,System Administrator"))
#print(re.search(r"(\d{3})-(\d{3})-(\d{4})", "Sabrina Green,802-867-5309,System Administrator"))
"""
