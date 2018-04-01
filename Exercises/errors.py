def division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Cannot be divided by zero"
print(division(1,0))
