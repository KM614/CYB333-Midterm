#This program will create a timer utility that can be used to measure the execution time of code blocks.

from timeit import default_timer as timer


# This functiuon will be used to time the execution of a function.

def timefunc(func):
    def inner(*args, **kwargs):
        start = timer()
        result = func(*args, **kwargs)
        end = timer()
        message = '{} took {} seconds' .format(func.__name__, end - start)
        print(message)
        return result
    return inner
