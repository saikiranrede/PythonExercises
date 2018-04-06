list = []
tempList = []
original = []
indices = []

def reverse(var):
    for item in var:
        original.append(item)
    for i in var:
        if(i.isalpha()):
            list.append(i)
        else:
            tempList.append(i)

    list.reverse()

    for spc in tempList:
        indices.append(original.index(spc))

    for nat, nit in zip(indices, tempList):
        list.insert(nat, nit)
    return list

def reverseString(dummy):
    result = reverse(dummy)
    final = ''.join(result)
    return "The reverse of the given string %s is: %s" % (dummy, final)

string = "adf$gydpjmw&v xt"
print(reverseString(string)+ "\n")

####### Input from commandline and differentiate str and other type #######

#value = input("Enter a string: ")
#if type(value) == str:
#    print(reverseString(value))
#else:
#    print("Please enter a string value")
