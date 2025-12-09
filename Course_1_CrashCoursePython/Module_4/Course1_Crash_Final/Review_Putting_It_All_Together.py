"""
-Function that grabs that date from the events object inputted.
-Function that returns the machines in use. It should create a machines dictionary, and if there's a login, add that machine to the dictionary. If there's a logout, it should remove that user from the dictionary. You can use the .add and input the events.machine object/attribute. That way you have a current list of machines. 
-Function called generate report which lists the machines a long with the user names listed. 
-Function called A class called Events which has the inputs: self, eventdate, eventtype, machinename, user.
-A List of events which has date & time together, login/logut, machinename (myworkstation, mailserver, webserver.local), username.
-
"""

def get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key=get_event_date)
        self.user = user

events = [
        Event('2020-01-21 12:45:46', 'login', 'myworkstation.local', 'jordan'),
        Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
        Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
        Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
        Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
        Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'chris')
]

users = current_users(events)
print(users)

generate_report(users)

