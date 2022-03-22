def mygenerator():
    yield 1
    yield 2
    yield 3


g = mygenerator()
for i in g:
    print(i)

g = mygenerator()
print(sum(g))

g = mygenerator()
value = next(g)
print(value)
value = next(g)
print(value)

g = mygenerator()
print(sorted(g))

def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

cd = countdown(5)

value = next(cd)
print(value)
print(next(cd))


import sys
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(sys.getsizeof(firstn(1000)))
print(sys.getsizeof(firstn_generator(1000)))


def fibonacci(limit):
    # 0 1 1 2 3 5 8 13 ...
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci(30)
for i in fib:
    print(i)


mygenerator2 = (i for i in range(1000) if i % 2 == 0)
print(sys.getsizeof(mygenerator2), type(mygenerator2))


