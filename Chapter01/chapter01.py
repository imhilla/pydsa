p = "Hello India"
q = 10
r = 10.2

print(type(p))
print(type(q))
print(type(r))
print(type(12 + 31j))

var = 13.2

print(var)
print(type(var))

var = 'No the type is a string'
print(var)

print(type(var))

# Data types
# Basic types numeric and boolean types

bool(False)
print(bool(False))
val1 = 11
print(bool(val1))

val2 = 0
print(bool(val2))

val3 = -19
print(bool(val3))

# sequence data types
# string range lists tuples

str1 = 'Hello how are you?'

# range data type
# range(start, stop, step)
print(list(range(10)))
print(range(10))
print(list(range(10)))
print(list(range(1, 10, 3)))
print(list(range(20, 10, -2)))


# lists
a = ["food", "bus", "apple", "queen"]
print(a)

# memebership, identity, logical operators
# membership ops include in not in

# identity operators
# are used to compare objects
# is is not
Firstlist = []
SecondList = []
if Firstlist == SecondList:
    print("Both are equal")
else:
    print("Both are not equal")

if Firstlist is SecondList:
    print("Both variables are pointing to the same object")
else:
    print("Both are not pointing to the same object")

ThirdList = Firstlist
if ThirdList is SecondList:
    print("Both variables are pointing to the same object")
else:
    print("Both variables are not pointing to the same object")

# logical operators
# and or not


# complex data types
# dictionaries and set data types
dict = {}

