correct_password = "python123"
name = input("Enter your name: ")
surname = input("Enter your surname: ")
password = input("Enter your password: ")
while correct_password != password:
    password = input("Wrong passwrod!!, Enter again: ")

message = "Hi %s %s, you're logged in" % (name, surname)
print(message)
