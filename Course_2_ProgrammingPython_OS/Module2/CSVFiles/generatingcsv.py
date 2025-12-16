#Like always, we need to import the csv file.
import csv

#Here we have a list of lists. Each little list just has the name of the host computer and it's IP Address. So I'm guessing we are gonna take this and make a CSV out of it. 
hosts = [["workstation.local", "192.168.2.2"], ["webserver.cloud", "10.2.5.6"]]

#Here we are making a file with the open function. It's a trick. If we set the functionn to "w" or write mode, it will make the the file if it's not here. Then we give this file a nickname at the end like hosts_csv.
with open("hosts.csv", "w") as hosts_csv:
    #I guess we have to create a CSV writer Object to start writing. And then plug in the name of the file we want to write to?
    writer = csv.writer(hosts_csv)
    #After that we can write each of the rows to the object. The writerows function will take a file and write down the info to it's rows.
    writer.writerows(hosts)
