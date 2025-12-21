"""
#Study Guide: Regular Expressions

#Advanced Regular Expressions - commonly reffered to as advanced regexes-are used by developers to execute complicated patterns matching against strings. In this reading, you will learn about some of the common examplesof advanced regular expressions.

#Alterations - an alteration matches any of the alternatives separted by the pip | symbol. Let's look at an example:

#r"location *(London|Berlin|Madrid)"
import re
#print(re.search(r"location.*(London|Berlin|Madrid)", "location is Madrid"))

#Matching only at the beginning or end.
#If you use the circumflex symbol (also known as a caret symbol)^ as the first character of your regex, it will match only if the pattern occurs at the start of the string.
#Alternatively, if you use the dollar sign symbol $ at the end of a regex, it will match only if the pattern occurs at the end. Let's look at a example:

#regex = r"^My name is (\w+)"
#Since there's a caret at the beginning, it matches "My name is Asha." but doesn't match "Hello. My name is Asha.".
#print(re.search(regex, "Hello. My name is Asha."))

#Character ranges
Character ranges can be used to match a single character against a set of possibilities. Let's look at a couple of examples.

r"[A-Z] This will match a single uppercase letter.

r"[0-9$-,.] This will match digits 0 through 9, the dollar sign, hyphens, commas, and periods.

This will match any phone number.
r"([0-9]{3}-[0-9]{3}-[0-9]{4})
See how it collects 3 numbers 3 numbers and then four. All with hyphens inbetween?

#Backreferences

A backreference is used when using a re.sub() to substitute the value of a capture group into the output. Let's look at an example:

re.sub(r"([A-Z])\.\s+(\w+)", r"Ms. \2", "A. Weber and B. Bellmas have joined the team.")

import re
print(re.sub(r"([A-Z])\.\s+(\w+)", r"Ms. \2", "A. Weber and B. Bellmas have joined the team."))

print(re.findall(r"([A-Z])\.\s+(\w+)", "A. Weber and B. Bellmas have joined the team."))

Oh I see. This is really tricky for each match it makes two groups which is a the Capital Letter and Lastname. The Capital Letter is the first group and the lastname is the second group.

So for each match it is going to substitute it for something else. In our case it is substituting for that new string "Ms. " plus the second group at the time of the match which is the lastname. So it is going through and replacing all the names with Ms. Lastname.

#Lookahead

If a lookahead matches a pattern only if it's followed by another pattern. Let's look at an example:

If the regex was r"(Test\d)-(?=Passed)" and the string was "Test1-Passed, Test2-Passed, Test3-Failed, Test4-Passed, Test5-Failed the output would be:
    Test1, Test2, Test4

?= is called a lookahead or scouter condition. So here we have to put ?=... and then something for the dots. In our case we put Passed and so it looked ahead at all our Test and told us which tests passed. Pretty handy.

Key Takeaways:
They types of advanced regular expressions explained in this reading are just some of the commonly used ones by developers. They are beneficial in pattern matching, text manipulating, and data validation. For more information, check out the following link:

Key Concepts:
-Matching at the beginning or at the End. Using ^ and $ symbols allows regex to match patterns specifically at the start and end of strings, enhancing precision. 
-Alterations - Alterations match any one of the alternatives separated by the pipe | symbol, allowing for flexible pattern matching. 
-Lookahead - Lookahead matches a pattern only if it is followed by another specified pattern, useful for conditional matching. 
-Character Ranges - Character ranges enable matching a single character against a set of possibilities, useful for validating input formats. 
-Backreferences - Backreferences allow the substitution of captured groups in regex, facilitating text manipulation. 

"""







