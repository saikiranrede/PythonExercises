""" Can use these kind of decorators for checking any criteria specified for any DBs or Admin page etc"""

import functools

def decorator_with_args(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_funs(*args, **kwargs):  #just in case the methods send any arguments
            print("Before decorator")
            if number == 56:
                print("Not running the functions")
            else:
                func(*args, **kwargs)
            print("After decorator")
        return function_that_runs_funs
    return my_decorator


@decorator_with_args(23)
def myFuncToo(x, y):
    print(x + y)

myFuncToo(5, 6)
