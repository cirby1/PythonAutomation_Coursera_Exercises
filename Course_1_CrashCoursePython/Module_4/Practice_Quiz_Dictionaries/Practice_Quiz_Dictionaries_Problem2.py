"""
The groups_per_user function receives a dictionary, which contains group names with the list of users. Users can belong to multiple groups. Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values. 
"""

def groups_per_user(group_dictionary):
    #Create a master group list.
    all_groups_list = []
    for groups, users in group_dictionary.items():
        for user in users:
            if user not in all_groups_list:
                all_groups_list.append(user)

    
    #Now I made a dictionary list for each group.
    group_collection_catalogue = {}
    for individual_group in all_groups_list:
        group_collection_catalogue[individual_group] = []

    user_groups = {}
    for groups, users in group_dictionary.items():
        for user in users:
            if groups not in group_collection_catalogue[user]:
                group_collection_catalogue[user].append(groups)
    user_groups = group_collection_catalogue
    return(user_groups)

print(groups_per_user({"local": ["admin", "userA"], "public": ["admin", "userB"], "administrator": ["admin"]}))

