import functools

"""
How the decorators works

def start_end_decorator(func):

    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper

def print_name():
    print('Chin')

print_name()

print_name = start_end_decorator(print_name)
print_name()
"""


def start_end_decorator(func):
    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper


@start_end_decorator
def print_name():
    print('Chin')


print_name()


def hello_goodbye(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("HELLO")
        result = func(*args, **kwargs)
        print("BYE")
        return result
    return wrapper


@hello_goodbye
def add5(x):
    return x + 5


a = add5(6)
print(a)
print(help(add5))
print(add5.__name__)


def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


@repeat(num_times=3)
def great(name):
    print(f"Hello {name}")

great("Jayden Chin")


def hi_bye(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("HI")
        result = func(*args, **kwargs)
        print("BYE")
        return result
    return wrapper


def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr +  kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper


@debug
@hi_bye
def say_hi(name):
    greeting = f"Hi {name}"
    print(greeting)
    return greeting


say_hi("Chin Wei Hong")


class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print('Hello')

say_hello()
say_hello()