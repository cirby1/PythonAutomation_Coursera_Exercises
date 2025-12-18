#A regular expression, sometimes called regex, is a string of characters that specifies a pattern to match against some text. In addition to matching patterns, they can search to extract specific parts of the text, validate input data, and are supported by code editors and integrated developmental environments. 

#Regex Examples

"""
r"\d{3}-\d{3}-\d{4}"


\d{3} - The engine looks for 3 digits in a row.

-    It then looks for a physical hyphen.

\d{3} - It looks for another 3 digits in a row. 

- It looks for another physical hyphen.

\d{4} - Finally it looks for four digits. This is the line number?

Okay so basically this looks for a phone number! Something I learned is that, the first three digits is the area code, the second three digits is the post office code, and the last four is the line code!!! That's pretty cool!!!!!!!!!!!!!!

"""

"""

r”^-?\d*(\.\d+)?$”

^ - Matches the start of the string. 

-   Is a physical hyphen to allow for negative numbers.

? - Means optional so the hyphen before is optional

\d* - Matches a single digit or more. 

() - A capturing group. All the symbols happen together or nothing at all. The symbols don't work independently. 

*Okay so quick note [] brackets are a buffet, parenthesis are a package deal.*

So \.\d+ - all work together to mean 
  \. a single decimal point
  \d - digits
  + one or more 

? - means that the decimal point part is also optional so they can be whole or decimal numbers. 

$ - Means look to the end of the input string. And there shouldn't be anything else. 

  So basically one or more digital decimal point.

So OVERALL this means an negative or positive number with as many decimals or not. The number can be a whole number or a decimal number.

Basically it looks for a number (positive, negative, or decimal) with no other characters or spaces allowed. 

"""


"""
r"^/(.+)/([^/]+)/$" 

^ - looked at the beginning of the line.

/ - means a physical forward slash like for a directory

(.+) - means look for one or more dots . WRONG the dot means anycharacter so it means one or more of any character! This is greedy to it's gonna pick up on anything even long file paths. It's kind of tricky I guess. 

/ - means another forward slash like a directory

([^/]+) - This means look for anyblock of continuous text as long as it's not a forward slash. 

/ - another literal forward slash. 

$ - Continue matching until the end of the string. 

#See if it starts with a slash, has a long set of characters and ends with some slash content slash. It can get a long url or even file path. Since the greedy part takes every character and will just end up stopping on whether the last /content/ is. And it will do this until the end of the string. Remember the greedy part keeps eating everything up until it realizes it has to leave at least one slash content slash at the end. So it goes all the way until it finds this. Oh and it makes sure theres a slash at the beginning and at the end.










"""
