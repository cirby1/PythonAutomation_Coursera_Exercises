#6. In the lab, you defined the replace_domains() function as:

    def replace_domain(address, old_domain, new_domain):
        old_domain_pattern = r"" + old_domain + "$"
        address = re.sub(old_domain_pattern, new_domain, address)
        return address

#What role does this function have in the process of updating outdated domain names with new domain names?

#A - To read data from a CSV file. - I'm not seeing any csv here. So no...
#B - To iterate over a list of email addresses. - This does iterate over the string, but not a list of addresses. It will iterate over the string that IS the address and see if it's an old domain pattern. If it is, then it will replace it with the new form.
#C - To replace the old domain with the new domain in an email address. - This is the one.
#D - To write the updated list to a CSV file. - Nope still no CSV...
