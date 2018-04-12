
""" Exercise where a list of people is entered as an input separated by commas
and then asked to enter user's name and checks whther he is in the list or not """

def who_do_you_know():
    list = []
    people = input("Enter the list of people you know: ")
    peopleList = people.split(",")  # also can be written [person.strip() for person in people.split(",")]
    for person in peopleList:       # Or [person.strip() for person in input("Enter the list of people you know: ").split(",")]
        list.append(person.strip())
    return list


def ask_user():
    user = input("Enter user's name: ")
    if user in who_do_you_know():
        return "User {} is in the list".format(user)
    else:
        return "User {} is not in the list".format(user)

print(ask_user())
