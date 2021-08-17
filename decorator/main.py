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

It is also possible to chain the decorators

def decor1(func): 
    def inner(): 
        x = func() 
        return x * x 
    return inner 
  
def decor(func): 
    def inner(): 
        x = func() 
        return 2 * x 
    return inner 
  
@decor1
@decor
def num(): 
    return 8
  
print(num())
> (8 * 2)**2 = 16 * 16 = 256


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
        # func:function is an object and has an attribute __name__
        print(f"Total execution time of {func.__name__} function is {end - begin}s")
        return result
    return inner

def negate_value(func):
    def inner(*args, **kwargs):
        return -1 * func(*args, **kwargs)
    return inner           


@calculate_time
def factorial(num: int) -> int:
    """
    this factorial function calculates the factorial of a given number
    """
    # sleep 2 seconds because it takes very less time to run the actual factorial
    time.sleep(2)
    return math.factorial(num)


''' 
chain of function decorator
which is the same to
foo = negate_value(foo)
foo = calculate_time(foo)

or
foo = calculate_time(negate_value(foo))
'''
@calculate_time
@negate_value
def negated_factorial(num: int) -> int:
    """
    this function calculates the negated value of the given number's factorial
    """
    # give some wait time
    time.sleep(2)
    return math.factorial(num)


def main():
    num = 3
    # runs alone 2.0005698204040527s
    # Hint: comment the following line to deactivate the interpreter cache 
    #       and see how the runtime of negated_factorial function increase.
    print(f"factorial of {num} is {factorial(num)}\n")
    # it is to notice, the interpreter caches the value of math.factorial(int), 
    # as single call, the negated_factorial runs in 2.0018250942230225s
    # that is 1ms longer than the call of decorated factorial function.
    print(f"negated factorial of {num} is {negated_factorial(num)}")


## == equal value, while "is" operator test the equal object 
if __name__ == "__main__":
    main()