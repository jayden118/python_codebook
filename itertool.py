# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators

from itertools import product, permutations, combinations, accumulate, groupby, count, cycle, repeat
import operator

a = [1, 2]
b = [3, 4]
c = product(a, b)
print(list(c))

a = [1, 2, 3]
perm = permutations(a)
print(list(perm))
perm = permutations(a, 2)
print(list(perm))

a = [1, 2, 3, 4]
comb = combinations(a, 3)
print(list(comb))

# accumulate
a = [1, 2, 3, 4]
acc = accumulate(a)
print(a)
print(list(acc))
acc = accumulate(a, func=operator.mul)
print(list(acc))
acc = accumulate(a, func=max)
print(list(acc))

# groupby
def smaller_than_3(x):
    return x < 3


a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)
group_obj = groupby(a, key=lambda x: x < 3)  # lambda is a one line function
for key, value in group_obj:
    print(key, list(value))

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]

group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))


# count
for i in count(10):
    print(i)
    if i == 20:
        break

# cycle
a = [1, 2, 3]
#for i in cycle(a):
#    print(i)

# repeat
for i in repeat(1, 4):
    print(i)