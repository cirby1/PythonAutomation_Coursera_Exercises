#5 - International Standard Book of Numbers (ISBN's) are used to uniquely identify published books. They follow a 13-digit format:

#      xxx-x-xx-xxxxxx-x

"""
where each X represents on numeric digit. You have a list of books, information about these books, and their ISBN numbers. You want to extract the 6 digits of the ISBN that come before the last hyphen of each book's ISBN number. However, you need to be careful to avoid 6 digit strings that are not a part of the ISBN numbers that you are interested in.

Complete the find_isbn() function so that you can use it to extract the 6-digit portion of the ISBN numbers of the books on your list.

"""
import re

result = re.search(r"(\d{3})-(\d)-(\d)-(\d{6})-(\d)", "The number is 333-4-5-777777-8")
print(result.groups())
print(result)
print(result.group(4))

"""
import re

def find_isbn(list):
    pattern = r"\d"
    print(result = re.sub(pattern,list, ))
    if result is None:
        return ""
    return result #Return the correct capture group here.

print(find_isbn("123-4-12-098754-0")) #Should return 098754
"""







