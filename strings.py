# Strings: ordered, immutable, text representation
from timeit import default_timer as timer

my_string = "I'm a programmer"
print(my_string)

my_string = "Hello World"
char = my_string[0]
char2 = my_string[-1]
print(char, char2)
print(my_string[:], my_string[:5], my_string[::2], my_string[::-1])

greeting = "Hello "
name = "Jayden"
sentence = greeting + name
print(sentence)

my_string = "      Hello World      "
print(my_string)
my_string = my_string.strip()
print(my_string)

print(my_string.startswith("Hello"))
print(my_string.endswith("d"))
print(my_string.find('e'))      # return letter index
print(my_string.count('l'))     # count occurance of letter in string
print(my_string.replace("World", "Universe"))

my_string = "how are you doing"
my_list = my_string.split(" ")
print(my_list)
new_string = ''.join(my_list)
print(new_string)

my_list = ["a"] * 6
print(my_list)

start = timer()
my_string = ''.join(my_list)
print(my_string)
stop = timer()
print(stop-start)

var = "Jayden"
my_string = "the variable is %s" % var
print(my_string)

var = 3.1234567
var2 = 6
my_string = "the variable is %d" % var
print(my_string)
my_string = "the variable is %f" % var
print(my_string)
my_string = "the variable is {:.2f} {}".format(var, var2)
print(my_string)
my_string = f"the variable is {var:.2f} and {var2}"
print(my_string)





