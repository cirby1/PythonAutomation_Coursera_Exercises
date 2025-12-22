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
    regex = r"(\w*)(@yahoo)(.com)"
    newemail = re.sub(regex,r"\1@gmail.com", oldemail)
    return newemail

with open("all_user_domains_start.csv", "r") as emails:
    myemails = csv.reader(emails)
    header = next(myemails)
    finished_emails.append(header)
    for row in myemails:
        print("Their email is: " + row[2])
        if "yahoo.com" in row[2]:
            print("We have an old email at:" + row[2])
            row[2] = change_email(row[2], "@yahoo.com")
            print("Their new email is: " + row[2])
        finished_emails.append(row)
        print()

for email in finished_emails:
    print(email)

with open("finished_emails.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(finished_emails)

