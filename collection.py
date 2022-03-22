# collections: counter, namedtuple, orderedDict, defaultdict, deque

from collections import Counter, namedtuple, OrderedDict, defaultdict, deque


a = "aaaaabbbbccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.values())
print(my_counter.keys())
print(my_counter.most_common(1))
print(my_counter.most_common(1)[0][0])

Point = namedtuple("Point", "x,y")
pt = Point(1, -3)
print(pt.x, pt.y)

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)

d = defaultdict(int)
d["a"] = 1
d["b"] = 2
print(d["c"])

dec = deque()
dec.append(1)
dec.append(2)
dec.appendleft(3)
print(dec)
dec.pop()
print(dec)
dec.popleft()
print(dec)
dec.extend([4, 5, 6])
print(dec)
dec.extendleft([4, 5, 6])
print(dec)
dec.rotate(2)
print(dec)
dec.rotate(-1)
print(dec)



