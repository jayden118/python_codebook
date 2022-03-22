# Dictionary: Key-value pairs, Unordered, Mutable

mydict = {"name": "Chin", "age": 32, "city": "Tokyo"}
print(mydict)

mydict_copy = dict(mydict)
mydict_copy2 = mydict.copy()

mydict["email"] = "chin@abc.com"

for key in mydict:
    print(key)

for value in mydict.values():
    print(value)

for key, value in mydict.items():
    print(key, value)

try:
    print(mydict["name"])
except:
    print("Error")

value = mydict["age"]
print(value)

del mydict["name"]
print(mydict)

mydict.pop("age")
print(mydict)

mydict.popitem()
print(mydict)

mydict = {"name": "Max", "age": 28, "email": "max@xyz.com"}
mydict2 = dict(name="Marry", age=27, city="Boston")

mydict.update(mydict2)
print(mydict)

