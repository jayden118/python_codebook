"""
- The difference between arguments and parameters
- Positional and keyword arguments
- Default arguments
- Variable-length arguments (*args, **kwargs)
- Container unpacking into function arguments
- Local vs. global arguments
- Parameter passing (by value or by reference?)
"""

def foo(a, b, c, d=4):
    print(a, b, c, d)


foo(a=1, b=2, c=3)
foo(c=1, b=2, a=3)
foo(1, 2, 3, 7)


def foo2(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])


foo2(1, 2, 3, 4, 5, six=6, seven=7)


def foo3(a, b, *, c, d):
    print(a, b, c, d)


foo3(1, 2, c=3, d=4)


def foo(a, b, c):
    print(a, b, c)


my_list = [1, 2, 3]
foo(*my_list)

my_dict = {'a': 1, 'b': 2, 'c': 3}
foo(**my_dict)


def foo():
    global number
    x = number
    number = 3
    print('number inside function: ', x)


number = 0
foo()
print(number)


result = 2 ** 4
print(result)

zeros = [0, 1] * 10
print(zeros)

stringAB = "AB" * 10
print(stringAB)


def foo(a, b, *args, **kwargs):
    print(a)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo(1, 2, 3, 4, 5, six=6, seven=7)


numbers = [1, 2, 3, 4, 5, 6]

*beginning, last = numbers
print(beginning)
print(last)

beginning, *last = numbers
print(beginning)
print(last)

beginning, *middle, last = numbers
print(beginning)
print(middle)
print(last)

beginning, *middle, secondlast, last = numbers
print(beginning)
print(middle)
print(secondlast)
print(last)

my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
my_set = {7, 8, 9}

new_list = [*my_tuple, *my_list]
print(new_list)

new_list = [*my_tuple, *my_set]
print(new_list)

dict_a = {'a': 1, 'b': 2}
dict_b = {'c': 3, 'd': 4}

my_dict = {**dict_a, **dict_b}
print(my_dict)





