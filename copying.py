"""
- Shallow copy : one level deep, only references of nested child objects
- deep copy : full independent copy
"""

import copy


# Immutable
org = 5
cpy = org
cpy = 6
print(cpy)
print(org)

# Mutable - warning
org = [0, 1, 2, 3, 4]
cpy = org
cpy[0] = -10
print(cpy)
print(org)

# Mutable - right way to copy
org = [0, 1, 2, 3, 4]
cpy = copy.copy(org)
cpy[0] = -10
print(cpy)
print(org)

cpy = org[:]
cpy[0] = -10
print(cpy)
print(org)

# Shallow copy
org = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy = copy.copy(org)
cpy[0][1] = -10
print(cpy)
print(org)

# deep copy
org = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy = copy.deepcopy(org)
cpy[0][1] = -10
print(cpy)
print(org)


# Shallow copy
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee


p1 = Person('Jayden', 33)
p2 = Person('Yuki', 27)

company = Company(p1, p2)
company_clone = copy.deepcopy(company)
company_clone.boss.age = 56
print(company_clone.boss.age)
print(company.boss.age)


