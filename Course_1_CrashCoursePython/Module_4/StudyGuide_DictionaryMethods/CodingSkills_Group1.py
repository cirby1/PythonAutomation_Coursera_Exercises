#This is the first Skills Group Coding Skills example in the Study Guide: Dictionary Methods. 

#Skill Group 1
#Iterate over the key and value pairs of a dictionary using a for loop with the dictionary.items() method to calculate the sum of the values in a dictionary. 

#Okay so from what I gather, this program will spit out the total time, in minutes represented in decimal form. So If you have an hour and a half, then it will spit out 1.5 hours. 

my_Server = {"User1":30.5345, "User2": 60.5111, "User3":100.133243}

def calculate_Total_Server_Time(insert_Server_Name):

    my_total_time = 0.0

    for key,value in insert_Server_Name.items():
   
        #Okay so it's going to cycle through and get the time for each user and then add it to the total time.
        my_total_time = my_total_time + insert_Server_Name[key]

        #We also need to round the total time. This little rounding method will take a number, and then you can specify the decimal places too. If you put 2 then it will round 2 decimal places. 
    my_total_time = round(my_total_time,2)

    return my_total_time

print(calculate_Total_Server_Time(my_Server))

#Okay, and that's the program. That's it. It just cycles over all the times, and adds them up and then spits out the total sum of all the times that people spend on a computer. *Voila!
