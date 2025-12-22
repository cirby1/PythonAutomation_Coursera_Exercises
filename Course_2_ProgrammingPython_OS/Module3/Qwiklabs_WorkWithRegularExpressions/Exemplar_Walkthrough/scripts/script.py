#In this lab you are given a CSV file of users with their domain names. You're job is to switch out the user's domains that have old domains with new ones.
#Afterwards, store all the domain names, including the new ones into a new file.

print("Starting my change email program...\n")
import csv
import re

finished_emails = []
oldformat = r"(\w*)(@yahoo)(.com)"

def change_email(str_oldemail, str_newdomain):
    oldemail = str_oldemail
    newdomain = str_newdomain
    regex = r"(\w*)(str_oldemail)(.com)"
    newemail = re.sub(regex,str_newdomain, oldemail)
    return newemail

with open("user_emails.csv", "r") as emails:
    myemails = csv.reader(emails)
    header = next(myemails)
    finished_emails.append(header)
    for row in myemails:
        print(row)
        if "yahoo.com" in row:
            print("yahoo is here")
            row = change_email("@yahoo.com", "@gmail.com")
        finished_emails.append(row)
        print()

for email in finished_emails:
    print(email)

with open("finished_emails.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(finished_emails)

