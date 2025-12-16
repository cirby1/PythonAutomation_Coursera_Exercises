#3 - In order to use the writerow() function of DictWriter() to write a list  of dictionaries to each line of a CSV file, what steps should we take?
#Create an instance of the DictWriter Class. - Yes we do, do this, and it's on line 12.
#Write the Fieldnames parameter into the first row using writeheader(). - No we didn't do this. The writeheader() function doesn't take any parameters and ill just write the header. After that we will write the rows as well and it will do both. Write the header and the rows.
#Open the csv file using with open. - Yes we did this on line 11.
#Import the OS module. No, we don't need this. Just the CSV module.

import csv
users = [{"name": "Sol Mansi", "username": "solm", "department": "IT Infrastructure"}]

keys = ["name", "username", "department"]

with open("by_department.csv", "w") as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)




