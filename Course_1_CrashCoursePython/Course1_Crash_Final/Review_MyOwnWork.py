"""
-Function that grabs that date from the events object inputted.
-Function that returns the machines in use. It should create a machines dictionary, and if there's a login, add that machine to the dictionary. If there's a logout, it should remove that user from the dictionary. You can use the .add and input the events.machine object/attribute. That way you have a current list of machines. 
-Function called generate report which lists the machines a long with the user names listed. 
-A class called Events which has the inputs: self, eventdate, eventtype, machinename, user.
-A List of events which has date & time together, login/logut, machinename (myworkstation, mailserver, webserver.local), username.
-
"""

#No the list is a list of sets of Event Objects. So it's a big list, which some sets in them, and inside the sets is the Event objects and information about each event. Okay... So I need to make the class first...


class Event:
    #Okay, I'm trying to refresh my memory on the class Event. And I need to set the variables for the class instance and have them equal to/plug into a logical naming attribute. So whatever they input for the event date for example will need to plug into something that makes sense like event date. 
    def __init__(self, inserted_event_date, inserted_event_type, inserted_machine_name, inserted_username):
        self.date = inserted_event_date
        self.type = inserted_event_type
        self.machine = inserted_machine_name
        self.username = inserted_username

    def printEventReport(self):
        #Okay, I got this working. I need to input the self attribute here in order to use self. Duh!
        #This will print info about the Event Object.
        print(self.date)
        print(self.type)
        print(self.machine)
        print(self.username)

#Okay, I was able to get the Event Class going. 
#myEvent = Event("12-02-2025 10:28", "Login", "Workstation.local", "Bobby")
#myEvent.printEventReport()

#Let's make some Events to cycle through:
events = [
Event("12-09-2025 10:29:05", "Login", "workstation.local", "Bobby"),
Event("12-09-2025 10:30:44", "Logut", "workstation.local", "Bobby"),
Event("12-10-2025, 12:00:02", "Login", "webserver.local", "Jim"),
Event("12-10-2025, 12:00:02", "Logout", "webserver.local", "Jim"),
Event("12-11-2025, 12:00:03", "Login", "mailserver.local", "Richard"),
Event("12-12-2025, 12:01:04", "Login", "mailserver.local", "Sally")
]

#We need a function that grabs the date from the Event object.
def getDate(input_event):
    #The input type for the input_event is the Event Class.
    #The output is going to the attribute for this event which is the date. 
    return input_event.date

#Okayyyyy, now we are onto the hard part. We need to make a fancy pants function here. One that, I forgot, let me yank it with Vim...

#-Function that returns the machines in use. It should create a machines dictionary, and if there's a login, add that machine to the dictionary. If there's a logout, it should remove that user from the dictionary. You can use the .add and input the events.machine object/attribute. That way you have a current list of machines. 

#Okay, so I need to make a dictionary that keeps track of the machines that are being used. The thing is, I don't know what it should input. All the events? Unless I get a nother function just to extract the name and machine. 
#This doesn't really make sense. Let me check...
def machinesUsed(input_Events):
    #I need to sort the events. 
    input_Events.sort(key=getDate)
    machines_in_use = {}
    for event in input_Events:
        #Here I need to do some logic. If the Event is a login. It gets put into the dictionary, If not then it gets removed. Otherwise, If there is no record of this machine is not in the machines list. Then start a blank set so that we can start keeping record. 
        if event.machine not in machines_in_use:
            #So here is the first check to see if we need to start an empty set for machines in use for that machine. 
            machines_in_use[event.machine] = set()
        if event.type == "Login":
            machines_in_use[event.machine].add(event.username)
        elif event.type == "Logout":
            machines_in_use[event.machine].remove(event.username)
    print(machines_in_use)
    return machines_in_use

def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{} {}".format(machine, user_list))

users = machinesUsed(events)
print(users)

generate_report(users)

