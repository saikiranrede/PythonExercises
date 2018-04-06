list = []
tempList = []
original = []
indices = []

def reverse(var):   #reverse function to get incoming list and reverse it in list format
    for item in var:
        original.append(item)  #keep the original
    for i in var:              #separate alphabets and spl chars
        if(i.isalpha()):
            list.append(i)
        else:
            tempList.append(i)

    list.reverse()             #reverse the list(alphabets) by using reverse functtion

    for spc in tempList:       #get the indexes of the spl chars in original list
        indices.append(original.index(spc))

    for nat, nit in zip(indices, tempList):  #zip the iterables indixes and their matching spl chars to try
        list.insert(nat, nit)                #to insert in the same indexes as before in the reversed list
    return list

def reverseString(dummy):
    result = reverse(dummy)
    final = ''.join(result)      #convert the list to the string
    return "The reverse of the given string %s is: %s" % (dummy, final)

string = "adf$gydpjmw&v xt"
print(reverseString(string)+ "\n")

####### Input from commandline and differentiate str and other type #######

#value = input("Enter a string: ")
#if type(value) == str:
#    print(reverseString(value))
#else:
#    print("Please enter a string value")
