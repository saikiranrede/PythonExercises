def simplified_addition(*args): #converts arguments to a list
    return sum(args)

def what_are_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

print(simplified_addition(1, 2, 3, 4, 5))

what_are_kwargs(1, 2, 3, 4, 5, name = 'Sai', school = 'MIT')
