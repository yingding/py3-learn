'''
TODO "function decorator" or "wrapper function"

# wrapper function has an inner function, which can be returned
# and the inner function consumes a function as parameter
# the wrapper function is a higher-order function
def wrapper(func):
    def inner(n):
	    func(n)
    Return inner;

@wrapper
def function(n):
    print(n)


is equivalent as

def funciton(n):
    print(n)

# reassign name or alias
function = wrapper(function)

# decorator factory with param
# https://stackoverflow.com/questions/5929107/decorators-with-parameters
# https://stackoverflow.com/questions/5929107/decorators-with-parameters/5929165#5929165
def decorator_factory(argument):
    def decorator(function):
        def wrapper(*args, **kwargs):
            funny_stuff()
            something_with_argument(argument)
            result = function(*args, **kwargs)
            more_funny_stuff()
            return result
        return wrapper
    return decorator

# it returns the function which returns the function object


'''

import time
import math

def calculate_time(func):
    """
    this higher-order function calculates and print out
    the execution time of the arg function
    """
    def inner(*args, **kwargs):
        # storing time before function execution
        begin = time.time()
        result = func(*args, **kwargs)
        # storing time after function execution
        end = time.time()
        print(f"Total execution time of {func.__name__} function is {end - begin}s")
        return result
    return inner    


@calculate_time
def factorial(num: int) -> int:
    """
    this factorial function calculates the factorial of a given number
    """
    # sleep 2 seconds because it takes very less time to run the actual factorial
    time.sleep(2)
    return math.factorial(num)


def main():
    # function is an object and has an attribute __name__
    # print(f"{main.__name__} is called.")
    num = 2
    print(f"factorial of {num} is {factorial(num)}")


## == equal value, while "is" operator test the equal object 
if __name__ == "__main__":
    main()