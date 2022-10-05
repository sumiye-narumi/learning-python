#Cross reference a pair of lists (Validation app given a stored user list, given an inputed list of users, return both name and position in the list)

ownerRosterList = ["Sumiye","Techno","Budviser"]

inputList = [item.strip() for item in input("Enter users seperated by commas: ").split(',')]

outputList = []

def crossRefLists(storedList, inputList):
    for name in inputList:
        if name in ownerRosterList:
            outputList.append({name: ownerRosterList.index(name)})
    print(outputList)

crossRefLists(ownerRosterList, inputList)