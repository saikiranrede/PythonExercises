def length_of_string(a):
    if(type(a)== int):
        return "Sorry, integers doesn't have length"
    elif(type(a)== float):
        return "Sorry, float types doesn't have length either"
    else:
        return len(a)


print(length_of_string(10.0))