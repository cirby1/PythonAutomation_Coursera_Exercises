"""
Okay I'm going to do the final project again, but this time with a little bit of gaming zeal. 
This is going to be a gamer tracker for online. I wanna make a program that will keep track of all the gamers that are currently online. 

But first I will need a task list of things to make. I need:
-A class to hold the gamers date of activity (both calendar and time all in one string, "type of activity whether they logged in or out", "type of console used for gaming", and their gamertag. 

-I will need to create all the gamer activity and store it into a list of objects. And each object will create the activity being tracked. 

- I need a function to grab the event date. 

-A need a function to tell me the current users online, this is the cream of the crop. It will have to sort the list of gamer activity by date, that way there's no confusion. Make a dictionary that will track current users. And then go through that entire gamer activity list and keep on adding/removing based on when they login/logout. At the end the gamers still logged in will remain. 

-At the end I will need to generate a report of each console and the users that are logged in for that console. I will need to print this line by line.

"""

class GamerLog:
    def __init__(self, timestamp, activity, console, gamertag):
        self.self = self
        self.timestamp = timestamp
        self.activity = activity
        self.console = console
        self.gamertag = gamertag


GamerActivities = [
        GamerLog("12-09-2025 2:15", "Login", "N64", "Joe95"),
        GamerLog("12-09-2025 4:00", "Login", "Xbox", "Jack"),
        GamerLog("12-10-2025 5:00", "Login", "Playstation", "SamEyeAm"),
        GamerLog("12-10-2025 5:00", "Login", "N64", "Cal"),
        #GamerLog("12-12-2025 6:00", "Logout", "Xbox", "Jack")
        ]

def getGamerDate(input_Gamer_Log):
    return input_Gamer_Log.timestamp

#This is the dictionary that keeps track of all the gamers. 
ledger_of_gamers = {}

for GamerActivity in GamerActivities:
    #print(GamerActivity.gamertag)
    #print(GamerActivity.console)
    if GamerActivity.console not in ledger_of_gamers:
        #This checks if the person's name is not in the tracker. 
        #This will create a blank slate If the gamer isn't in the tracker of gamers. 
        #Okayyyy, It's working after running and printing the items in the dictionary. Next part...
        ledger_of_gamers[GamerActivity.console] = set()
    if GamerActivity.console in ledger_of_gamers and GamerActivity.activity == "Login":
        ledger_of_gamers[GamerActivity.console].add(GamerActivity.gamertag)
    elif GamerActivity.gamertag not in ledger_of_gamers and GamerActivity.activity == "Logout":
        ledger_of_gamers[GamerActivity.console].remove(GamerActivity.gamertag)
print(ledger_of_gamers.items())





