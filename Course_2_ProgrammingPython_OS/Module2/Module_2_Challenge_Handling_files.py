"""
#1 - What is the characteristic of a CSV File?
A. It cannot be read by a text editor. - This isn't true as I used Vim to open a CSV file.
B. Each line represents a different column of data. - I think every comma separation represents a comma. Each line represents a row.
C. CSV files can contain only numeric data. - this isn't true because we have strings of data like employee data names.
D. Data in each row is separated by a special character. - this is most likely true because you can separate by commas, spaces, and maybe even semicolons?
#My answer is D here.

#2 - You and your colleagues frequently work in a folder containing thousands of automatically generatred files. One day you discover that you cannot write to any of the files in the folder. What is the likely cause of this?
A. Someone wrote a script that used with open() to write to all the files and forgot to close them. - I don't this right because with open automatically closes them.
B. Someone wrote a script that used open() to write all the files and forgot to close them. - This seems like the most likely answer as you could use the open function and forget to close the files. 
C. Your file permissions expired. - I don't think file permissions "expire" they are just set it and forget it. You may not just have them. 
D. Your disk is corrupted.  - I don't think it's this one. It's kind of written like a silly answer.
#My answer is B. 

#3 - On a Windows file system, C:\Users\Home\Documentsreport.docx is an example of what kind of file path? 
A. Absolute File Path - I think this is th answer since it's explicitly stating the drive and the folders and subfolders one has to look through to get to the file.
B. Relative file Path - I think these types of file paths just use the current file folder. 
C. Relational - there isn't any such thing as a relational
D. None of the above - Again, I think it's an absolute path.
#My answer is A. Absolute Path. 

#4 - Which of the following statements using the os module will return True if a file called output.txt exists in the current working directory and False if it does not?
#My answer is D: os.path.exists("output.txt")

#5 - What happens if you open() function in "w" mode on a existing file?
A. - Whatever you write will be written beneath the existing content. - Beneath? No that's really even possible. Text doesn't stack on each other in a text file.
B. - The old contents will be deleted as soon as the file is opened. - I think it's this.
C. - You will get an error for trying to write an existing file. - I didn't get an error when doing this.
D. - You will be prompted to either overwrite the file's existing contents or append them. - I didn't get a prompt. And a text file or Python3 isn't as sophisticated as that.
#Okay I tried writing and all the contents 

#6 - Imagine you're reading a text file line by line in Python. The file contains data like names, but each name has an extra line appended after it. Which of the following modifications to the code would most effectively remove these extra blank lines while keeping the names intact?
A. - Use a loop to iterate through each character in the line and remove any newline characters.
B. - Add an if statement within the loop to only print lines that are not empty. 
C. - Open the file in write mode and rewrite the contents without the blank lines. 
D. - Apply the strip() method on each line before storing it in a list. 
#This one is tough. I feel like since they like to show off and use all this Python functionality it's going to be D. which uses the strip() method. 

#7 - On Linux Systems, which of the following commands is used to create a new directory?
A. mkfolder directory_name
B. create directory_name
C. mkdir directory_name
D. newdir directory_name
#It's C. I already know this one.

#8 - When working with CSV files in Python, how can you efficiently convert the data into a format that allows you to access information by column names (like keys in a dictionary)?
A. Use the csv.DictReader class from the csv module. - I think it's this one. Since we've used this command a lot.
B. You need to manually write code to loop though each row and create dictionaries yourself. - Don't think so if there's DictReader class.
C. There's no direct way to achieve this; CSV files remain as list of lists. - That's not true. We just did a whole lab on this.
D. The standard csv.reader() function automatically converts CSV data into dictionaries. - It doesn't automatically convert into a dictionary with .reader(). This just reads the entire csv into memory. It still isn't a dictinary yet.
#My answer is A. 

#9 - Why is it useful to verify whether a file exists? Select all that apply. 
A. - It helps avoid getting a "file not found" error If you try to operate on a non-existent file.
B. - It helps prevent accidently overwriting an existing file.
C. - It helps you find files when you don't remember their exact name.
D. - You cannot write to any file unless you first verify that it exists.
#I'm not sure on this one. I think A is right. It's an error in the Python debugging error messages. B is useful as well. C. Doesn't make sense since If you don't know their name, how can you verify them? D. Isn't true because you write to a nonexistent file and it will create one.
#I think it's A and B...

#10 - The Python code snipped below processes data from an open CSV file and stores it in a list named employee_list. What does line 3 achieve within the loop?
employee_list = []
for data in employee_file:
    employee_list.append(dict(data))

A. It creates a new dictionary for each data item and discards the original data. - Nope there's only a list and a list operation here.
B. It converts each data item from the file into a dictionary and appends it to the employee_list. - This one looks good...
C. It merges the contents of the file directly into the employee_list variable without any changes. - Nope, no merging here..
D. It appends each line of the file (as a string) to employee_list without modification. - This is wrong. It's gonna append each line as a dictioanry. And create a list of dictionaries, just like in the lab.
#I think it's B. 





"""
