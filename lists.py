# Lists: ordered, mutable, allows duplicate elements
mylist = [4, 3, 1, -1, -5, 10]
print(mylist)

new_list = sorted(mylist)
print(new_list)

mylist = [0] * 5
print(mylist)

mylist2 = [1, 2, 3, 4, 5]

new_list = mylist + mylist2
print(new_list)

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = mylist[1:5]
print(a)
a = mylist[1::]
print(a)

list_org = ["banana", "cherry", "apple"]

list_cpy = list_org.copy() # list(list_org) list[:]
list_cpy.append("lemon")

print(list_cpy)
print(list_org)

mylist = [1, 2, 3, 4, 5, 6]
b = [i*i for i in mylist]
print(mylist)
print(b)



