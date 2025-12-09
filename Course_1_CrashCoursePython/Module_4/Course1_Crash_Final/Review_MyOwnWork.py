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
myEvent = Event("12-02-2025 10:28", "Login", "Workstation.local", "Bobby")
myEvent.printEventReport()

#Let's make some Events to cycle through:
events = [
Event("12-09-2025 10:29:05", "Login", "workstation.local", "Bobby"),
Event("12-09-2025 10:30:44", "Logut", "workstation.local", "Bobby"),
Event("12-10-2025, 12:00:02", "Login", "webserver.local", "Jim"),
Event("12-11-2025, 12:00:03", "Login", "mailserver.local", "Richard")
]

#We need a function that grabs the date from the Event object.
def getDate(input_event):
    #The input type for the input_event is the Event Class.
    #The output is going to the attribute for this event which is the date. 
    return input_event.date




