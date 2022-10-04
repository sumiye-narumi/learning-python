    # Define a function that given a list of values and a value to search for, will return true if the value is in the list. Otherwise return false.

List1 = [1,2,3]

def verifyInList(testList,searchFor):
    if searchFor in testList:
        print(str(searchFor) + " is true")
    else:
        print(str(searchFor) + " is false")

verifyInList(List1,2)
