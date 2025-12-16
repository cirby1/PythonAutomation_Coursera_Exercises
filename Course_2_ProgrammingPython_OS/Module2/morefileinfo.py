"""
import os

print(os.path.getsize("spider.txt"))

print(os.path.getmtime("spider.txt"))
"""

"""
import os
import datetime
timestamp = os.path.getmtime("spider.txt")
print(datetime.datetime.fromtimestamp(timestamp))
print()
print(os.path.abspath("spider.txt"))
"""

import os
#os.mkdir("newer_dir")
#os.rmdir("newer_dir")
#os.mkdir("newer_dir")

os.listdir("website")

dir = "website"
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))








