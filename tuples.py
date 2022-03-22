# Tuple: ordered, imutable, allows duplicate elements
import sys
import timeit

mytuple = ("Chin", 28, "Boston")
print(mytuple, type(mytuple))

for i in mytuple:
    print(i)

if "Chin" in mytuple:
    print("YES!")
else:
    print("NO!!")

my_tuple = ('a', 'p', 'p', 'l', 'e')
print(my_tuple, len(my_tuple), my_tuple.count('p'), my_tuple.index('p'))

name, age, city = mytuple
print(name, age, city)

my_tuple2 = (1, 2, 3, 4, 5)

e1, *e2, e3 = my_tuple2
print(e1)
print(e2)
print(e3)

my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(mytuple), "bytes")

print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4 ,5)", number=1000000))


