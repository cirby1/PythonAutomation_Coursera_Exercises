#Here are the notes from the Python in Action. Geez. This is taking freaking forever. 

"""
Well anyways to beat the freaking horse to death. I built a Python script from the ground up literally. I did this though by copying them, and then creating my own creative version of it. It helped me understand what was going on a little bit more. I feel like I still need a little bit more practice with mixing all these data types. And geez! Python is awful with data types and all this walk like a duck typing business. 

I think I might start declaring my data types in my variables, and also the input and output of my functions, because geez it's a headache.

Well anyways, I got to:

-Isolate a problem.

-Researched the tools needed to solve a problem.

-Planned an approach or best strategy to figure out what needs to be done, how it's done, and how to structure the code.

-Write a script to solve a problem.

-Run and check that the code works the way it should.

"""

"""
The Problemo and soluchion. (Is that Spanish? I dunno)

Imagine this scenario, Every Month, you are handed a spreadsheet with hundreds of new hires. Okay, got it a whole list of new people...

You are asked to create user accounts for all of them on a Linux server. Okay! That sounds awesome! Anything Linux and I'm game. 

The formatting on the Spreadsheet looks like this:

username, password, real_name

amanda,,Amanda Alonso

ian,,Ian Ortega

eugene,,Eugene Konya

[...] This little box with three dots represent a series and means it's ongoing in the same pattern I'm guessing. 

The password field is empty for all the records. So you will need to generate passwords for all the users and create their accounts. You also want to write the passwords you generate into a CSV, so that you can tell your employers their passwords. 

This task isn't difficult. It's just time intensive, especially If you create passwords and accounts for hundreds of new hires one by one. Your solution is to automate the task with Python. 

THE SCRIPT

To automate the task of creating passwords and accounts for all these new hires, the script should be the following: 

- Read a list of new_hires from users_in.csv.

- Generate a random 16-character passwords for each user.

- Create each user account.

-Write the spreadsheet back to users_out.csv with the new passwords. 

Your Tools:

To help organize all the data, create accounts for the new hires, and create passwords for each new user, you first need to import a few standard Python Libraries. 

import csv 

This library helps you read and write csv files. 

import secrets

This help generates random passwords for each user account.

import subprocess

This calls the useradd command, which creates and adds each user account. 

from pathlib import Path # to locate the data files

This library helps to locate the data files for each user account. 

"""

#Here's the code written out below:

#This library helps with reading and writing csv files.
import csv

#This helps with generating random passwords for users. 
import secrets

#This calls the useradd command, which creates and adds each user account.
import subprocess

#This command helps locate the data files for each user account. 
from pathlib import Path # to locate the data files

#After importing the libraries  that help you execute the script, you need to get the current working directory and find the subdirectory where the CSV files are stored. Use cwd for "current working directory" and identify the path of the Python directory as a string.
cwd = Path.cwd()

#Next, you use a with statement and an "as" keyword. The with statement helps with resource management, and the as keyword creates an alias for the resource you want to call. Consider the following code: 
with open(cwd / "data/users_in.csv", "r") as file_input, open(cwd / "data/users_out.csv", "w") as file_output:

    #The CSV library takes care of reading and parsing from input from the file. Next, you can use DictReader object so that each row in the file is read into dict() with the field names and values, like this: ["username": "amanda", "password": "", "real_name": "Amanda Alonso"]
reader = csv.DictReader(file_input)

#The input or the script is now complete! Now you need to setup the output. You create a DictWriter and use the same field fro the input, like so:
writer = csv.DictWriter(file_output, fieldnames=reader.fieldnames)
writer.writehead()

#Next, you create a for loop to run through each record from the input file:
for user in reader:
    #After the for loop, you use the secrets library that you imported at the beginning of the script to generate a random password of eight bytes, which equals 16 characters in total. Then, run the /sbin/useradd command to create each user. The check=True parameter causes the script to exit with a CalledProcessError if the command fails for any reason.
    user['password'] = secrets.token_hex(8)
    useradd_cmd = ["/sbin/useradd"]
                    "-c", user["real_name"],
                    "-m",
                    "-G", "users",
                    "-p", user["password"],
                    user["username"]]
    subprocess.run(useradd_cmd, check=True)
    
    #Finally, you write the records back to the output file, including the passwords. When you run the code, the new user accounts, and their passwords are generated into a new CSV file. 
    writer.writerow(user)

#After the script runs, the output file looks something like the following below. There was an image. But I'm using the command line to do all of this. 
"""
|username|password|real_name|
_____________________________
jim      |dkk3jkjfkdjf        |James T. Kirk
"""

#I'm not gonna write the rest. 
#And there you have it. You will save yourself countless hours having to create hundreds of new employee accounts and passwords by creating a short, simple script to do the work for you.

#Key Takeaways
#There are many real-world applications for using Python: creating programs, solving complex problems, simplifying and/or automating time-intensive tasks, and many more. But the process always remains the same-identifying a problem, coming up with a solution, determining the tools that help you achieve your solution, as well as the most significant part-writing the actual script! As you saw in this example, any time you have a repetitive task, think of using Python to automate the task. The programming skills you learned can make the work you do in your IT job a lot faster and more efficient. 


"""
Key Concepts:
-Random Password Generation: Utilizing the secrets library to create secure, random passwords for user accounts. 
-Subprocess Module: Employing the subprocess module to execute system commands for user account creation. 
-Automation: The process of using programming to perform tasks automatically, reducing manual effort and time. 
-CSV File Handling: Using Python's csv library to read from and write to CSV files, which are essential for data management in this task.
-Problem Statement: A clear definition of the issue to be solved, such as creating user accounts for new hires. 
"""






