def my_method(another_method):
    return another_method()

def addition():
    return 15+16

print(my_method(addition))

#using a lambda funtion (anonymous) and always in one line
print(my_method(lambda: 23+45))

my_list = [1, 4, 5, 3, 2, 6]

print(list(filter(lambda x : x != 3, my_list)))

print((lambda x : x*3)(5))

print([x for x in my_list if x != 3])  #list comprehension
