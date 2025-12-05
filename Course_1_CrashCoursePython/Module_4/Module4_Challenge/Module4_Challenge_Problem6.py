"""
Start Here:

Consider the following scenario about Python Dictionaries: 

Tessa and Rick are hosting a party. Together, they sent out invitations, and collected the responses in a dictionary, with names of their friends and the number of guests each friend will be bringing. 

Complete the functions so that the "check_guests" function retrieves the number of guests (value) the specified friend "guest" (key) is bringing. This function should:

1. Accept a dictinary "guest_list" and a key "guest" variable pass through the function parameters.

2. Print the values associated with the key variable. 

"""

invitations = {"Bob": 33, "Sarah": 32, "Stacy": 17, "Matt": 14}



def check_guests(guest_list, guest):
    return guest_list[guest]

print(check_guests(invitations, "Bob"))

     





