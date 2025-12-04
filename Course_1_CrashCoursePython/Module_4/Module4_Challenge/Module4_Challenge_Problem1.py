"""
The format of the input variable "address_string" is: numeric house number, followed by street name which may contain numbers, and could be several words long (e.g. "123 Main Street", "1001 1st Ave", or "55 North Center Drive").
Complete the string methods needed in this function so that input like "123 Main Street" will produce the output "House Number 123 on a street named Main Street". This function should include the following:

1. accept a string through the parameters 

2. Separate the address string into new strings: house_number and street_name;

3. Return the variables in the string format: "House number X on a street named Y". 
"""

def address_calling(input_string):
    split_address_parts = input_string.split()
    house_number = ""
    street_name = ""
    for individual_part in split_address_parts:
        if individual_part.isalpha():
            street_name = street_name + " " + individual_part
        else:
            house_number += individual_part
    
    return "House number {} on a street named {}.".format(house_number, street_name)

print(address_calling("456 Cursive Drive"))

#Okay, overall I think this is a good solution. And I will be using what I learned here to finish problem 1. 

"""
def format_address(address_string):

    house_number = ""
    street_name = ""


    # Separate the house number from the street name.
    address_parts = address_string.split()
    
    for address_part in address_parts:
       # Complete the if-statement with a string method.  
       if address_part.isnumeric():
         house_number = house_number + address_part 
       else:
         street_name = street_name + " " + address_part
    # Remove the extra space at the end of the last "street_name".
    street_name = street_name.strip()
 
    # Use a string method to return the required formatted string.
    return "House number {} on a street named {}.".format(house_number, street_name)


print(format_address("123 Main Street"))
# Should print: "House number 123 on a street named Main Street"


print(format_address("1001 1st Ave"))
# Should print: "House number 1001 on a street named 1st Ave"


print(format_address("55 North Center Drive"))
# Should print "House number 55 on a street named North Center Drive"
"""




