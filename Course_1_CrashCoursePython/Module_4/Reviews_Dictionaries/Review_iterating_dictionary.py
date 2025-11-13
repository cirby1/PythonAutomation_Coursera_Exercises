"""
file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}

for extension in file_counts:
	print(extension)
"""

"""
file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for ext, amount in file_counts.items():
    print("There are {} files with the .{} extension".format(amount, ext))
"""

"""
file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for ext, amount in file_counts.items():
    print("There are {} files with the .{} extension".format(amount, ext))
"""

"""
file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
#print(file_counts.items())
for value in file_counts.values():
    print(value)
"""

def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0 
        result[letter] += 1
    return result

#print(count_letters("aaaaa"))
#print(count_letters("tenant"))
print(count_letters("a long string with a lot of letters"))











