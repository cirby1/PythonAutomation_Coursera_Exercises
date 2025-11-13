"""
message = "A kong string with a silly typo"
message[2] = "l"
#Throws Error.
"""

"""
message = "A kong string with a silly typo"
print(message[0:2])
print(message[3:])
new_message = message[0:2] + "l" + message[3:]
print(new_message)
"""

"""
message = "This is a new message"
print(message)
message = "And another one"
print(message)
"""

"""
pets = "Cats & Dogs"
print(pets.index("&"))
print(pets.index("C"))
print(pets.index("Dog"))
print(pets.index("s"))
"""

"""
pets = "Cats & Dogs"
#pets.index("x")
#This will throw an error.
print(pets.index("D"))
"""

"""
pets = "Cats & Dogs"
print("Dragons" in pets)
print("Cats" in pets)
print(pets)
"""

def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

print(replace_domain("cal@yahoo.com", "yahoo.com", "gmail.com"))

















