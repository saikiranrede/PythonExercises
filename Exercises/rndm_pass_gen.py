import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'

def pass_char(value):
    password = ''
    for item in range(value):
        password += random.choice(chars)
    return password

value = input("Enter a value for number of chars for pass: ")
print(pass_char(int(value)))
