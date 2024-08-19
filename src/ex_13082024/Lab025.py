# strings
name = "Preeti"
print(type(name))
print(name.upper())
print(name.lower())
print(len(name))

a = "90"
age = 90
print(type(a))
print(type(age))

name = "This is a big name"
print(type(name))
# name = name + 1 ----can only concatenate str (not "int") to str,
# but we can do as below
name = name + "1"
print(name)
# OR
name = name + str(2)
print(name)

first_name = "Preeti"
last_name = "Chougule"
full_name = first_name + last_name  # Concatenation
print(full_name)

how_many_planes_i_have = None
print(type(how_many_planes_i_have))  # this is NoneType
# Null is not present in python

val = 9  # this is an int
# id - Identity
age = 10
age2 = 11
print(id(age))  # Return the identity of an object
print(id(age2))  # Return the identity of an object
# (CPython uses the object's memory address.)
