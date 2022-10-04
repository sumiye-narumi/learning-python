# Variables

    # Double Quotes or Single Quotes to make strings out of text
var1 = "Text1"
var2 = 'Text2'

    # Numbers are Intigers
var3 = 123
var4 = 456

    # Float (Decimil Value)
var5 = 1.5

print(var1)
print(var2)

    # Just combines the Text
print(var1 + var2)

    # Adds the Intigers
print(var3 + var4)

    # str converts Intiger to String
print(var1 + str(var3))

    # Defining a function
def potato():
    return "potato"

    #
print(potato() + var1)

    # f is a formatted string inputing direct values
def potato2(input):
    return f"potato {input}"

print(potato2(var1))

def potato3(input,input2,input3):
    return f"potato {input}, {input2}, {input3}"

print(potato3(var1,var1,var2))

# == if equal to

varList = []

def test1(input,input2,input3):
    varList.append(input)
    varList.append(input2)
    varList.append(input3)

test1(var1,var2,var2)

print(varList)