# lambda arguments: expression
from functools import reduce


add10 = lambda x: x + 10
print(add10(5))

mult = lambda x,y: x*y
print(mult(2, 7))

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D) # sort first element
points2D_sorted2 = sorted(points2D, key=lambda x: x[1]) # sort second element
points2d_sorted3 = sorted(points2D, key=lambda x: x[0] + x[1])
print(points2D)
print(points2D_sorted)
print(points2D_sorted2)
print(points2d_sorted3)

# lambda arguments: expression
# map(func, seq)
a = [1, 2, 3, 4, 5, 6]
b = map(lambda x: x*2, a)
print(list(b))

c = [x*2 for x in a]
print(c)

# filter(func, seq)
b = filter(lambda x: x % 2 == 0, a)
print(list(b))

c = [x for x in a if x % 2 == 0]
print(c)

# reduce(func, seq)
product_a = reduce(lambda x, y: x*y, a)
print(product_a)

