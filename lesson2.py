#Cross reference a pair of lists (Validation app given a stored user list, given an inputed list of users, return both name and position in the list)

ownerRosterList = ["Sumiye","Techno","Budviser"]

userList = [item.strip() for item in input("Enter users seperated by commas: ").split(',')]

outputList = list(set(ownerRosterList).intersection(userList))

print(outputList)