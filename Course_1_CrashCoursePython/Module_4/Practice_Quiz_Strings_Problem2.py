#Using the format method, filll in the gaps in the convert_distance function so that it returns the phrase "X miles equals Y km", with Y ahving only 1 decimal place. For example, convert_distance should return "12 miles equals 19.2 km". 
import math
def convert_distance(miles):
    km = miles * 1.6
    km = math.floor(km*10)/10
    result = "{} miles equals {} km".format(miles, km)
    return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km.

#Okay, well I did the work. And did the best that I could. It's giving me single decimal places. 
