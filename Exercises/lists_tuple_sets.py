grades = [77, 80, 90, 95, 100]
grades_tup = (77, 80, 90, 95, 100)

print(len(grades))
print(sum(grades)/len(grades))

lottery_numbers = {1, 2, 3, 4, 5, 6}
winning_numbers = {1, 3, 5, 7, 9, 11}

# Set methods same as set methods from math
print(lottery_numbers.intersection(winning_numbers))
print(lottery_numbers.union(winning_numbers))
print(lottery_numbers.difference(winning_numbers))
