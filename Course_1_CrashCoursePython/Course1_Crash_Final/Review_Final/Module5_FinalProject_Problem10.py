#Last Problem!!!!!!!!!!!!!!!!
#10. What is the purpose of the following code snippet?

#Looks like it takes a dictionary as input.
def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{} {}".format(machine, user_list)

#It cycles through all the items in the dictionary and formats the users to be displayed. It shows the machines that are logged in and who is logged into them line by line. 

#To create a list of all users currently logged into any machine and the machine they're logged into.
#To create a list of all users who have ever logged into any machine.
#To print a list of all the machines that are currently in use.
#To print a list of all the events that have occured. 

#It's not creating a list. And it's not printing all the information just the machine and the user. It's C. 


