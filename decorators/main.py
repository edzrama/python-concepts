import functools


def my_decorator(func):
    def wrapper():
        print('Hello')
        func()
        print('and the Universe')

    return wrapper


@my_decorator
def test_print():
    print('World')


# if decorator is not used, function should look like this:
# test_print = my_decorator(test_print)
test_print()


#  decorator with inner function arguments
def my_decorator_with_arg(func):
    def wrapper(*args, **kwargs):
        print('Processing')
        sum_it = func(*args, **kwargs)
        print('Completed')
        return sum_it

    return wrapper


@my_decorator_with_arg
def addition(x, y):
    return x + y


result = addition(10, 5)
print(result)


# the functools.wraps decorator will preserve the information about the original function.
def my_decor(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        sum_it = func(*args, **kwargs)
        print('End')
        return sum_it

    return wrapper


@my_decor
def add_5(x):
    return x + 5


result = add_5(10)
print(result)
print(add_5.__name__)
help(add_5)


# Decorator function with arguments
def repeater(num):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                ret = func(*args, **kwargs)
                print('repeater')
            return ret

        return wrapper

    return decorator_repeat


@repeater(num=3)
def greet(name):
    print(f"Hello there {name}")


greet('Edz')


# Nested Decorators
# a decorator function that prints debug information about the wrapped function
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Debug decorator: {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result

    return wrapper


# Multiple decorators
@debug
@repeater(num=4)
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting


# now `debug` is executed first and calls `repeater`, which then calls `say_hello`
say_hello(name='Edz')


# Class decorator
class CountCalls:
    # the init needs to have the func as argument and stores it
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    # extend functionality, execute function, and return the result
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)


@CountCalls
def say_hello(num):
    print("Hello!")


say_hello(5)
say_hello(5)
