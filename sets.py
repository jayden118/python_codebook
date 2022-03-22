# Sets: unordered, mutable, no duplicates

myset = {1, 2, 3}
print(myset)

myset = set("Hello")
print(myset)

myset = set()

myset.add(1)
myset.add(2)
myset.add(3)

for i in myset:
    print(i)

print(myset.pop())
myset.remove(3)
myset.discard(2)
myset.clear()

print(myset)

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

unions = odds.union(evens)
print(unions)

intersections = odds.intersection(evens)
print(intersections)

intersections = odds.intersection(primes)
print(intersections)

intersections = evens.intersection(primes)
print(intersections)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

difference = setA.difference(setB)
print(difference)

difference = setB.difference(setA)
print(difference)

sym_difference = setB.symmetric_difference(setA)
print(sym_difference)

sym_difference = setA.symmetric_difference(setB)
print(sym_difference)

setA.update(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.intersection_update(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setB.intersection_update(setA)
print(setB)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.symmetric_difference_update(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setB.symmetric_difference_update(setA)
print(setB)

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
print(setA.issubset(setB), setB.issubset(setA))
print(setA.isdisjoint(setB))
print(setA.issuperset(setB), setB.issuperset(setA))




