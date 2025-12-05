"""
#3 - Consider the following scenario about using Python lists:

    A Professor gave his two assistants, Aniyah and Imani, the task of keeping an attendance list of students in the order they arrived in the classroom. Aniyah was the first one to note which students arrived, and then Imani took over. After Class, they each entered their lists into the computer and emailed them to the professor. The professor wants to combine the two lists into one and sort it in alphabetical order. 
    Complete the code by combining the two lists into one and then sorting the new list. This function should:

    1. Accept two lists through the functions parameters.
    2. Combine the two lists.
    3. Sort the combined list in alphabetical order.
    4. Return the new list. 
"""

Aniyah_List = ["Zeffrey", "Amy", "Bob", "Xavier", "Clark", "Danielle", "Evelyn", "Frank"]
Imani_List = ["George", "Hank", "Rickie", "Israel", "Jacob", "Kevin", "Lauretta"]
#combined_list = Aniyah_List
#combined_list = Aniyah_List + Imani_List
#print(combined_list)
#Okay, so this definitely works. 

def combine_lists(input_firstlist, inputsecondlist):
    combine_lists = input_firstlist + inputsecondlist
    combine_lists.sort()
    return combine_lists

print(combine_lists(Aniyah_List, Imani_List))




