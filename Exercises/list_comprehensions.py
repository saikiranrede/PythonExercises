my_list = [0, 1, 2, 3, 4]
an_equal_list = [x for x in range(5)] # creates a list for x in range 5 i.e., [0, 1, 2, 3, 4, 5]

multiply_list = [x*3 for x in range(5)]

evens = [n for n in range(10) if n%2 == 0]

people = ["Sai", "kiran", "REDDY", " Pothula"]
normalized_people = [person.strip().lower() for person in people]

print(an_equal_list)
print(multiply_list)
print(evens)
print(normalized_people)
