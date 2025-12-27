#6 - In the provided code snippet, what is the purpose of the replace_domain() function?
def replace_domain(address, old_domain, new_domain):
    old_domain_pattern = r'', + old_domain + '$'
    address = re.sub(old_domain_pattern, new_domain, address)
    return address

#So it's asking what the purpose of this function is? I'm guessing it's to replace an old domanin address with a new one.
#A - To extract the username of an email address. - nope not useranmes
#B - To validate the format of an email address. - maybe
#C - To create a new email address by replacing an old domain with a new domain. - This is the one
#D - To remove any domain from the email address. nope since it's substituting with a new one and assigning this new value to address.


