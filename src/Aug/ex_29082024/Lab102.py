# Set  - is collection of unique elements, defined with {}

t = ("TheTestingAcademy", "for", "TheTestingAcademy")
print(t)
set1 = set(t)
print(set1)

set1 = {1, 2, 3}
set2 = {4, 5, 6}
my_set = set1.union(set2)
print(my_set)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
my_set = set1.intersection(set2)
print(my_set)

my_set = set1.difference(set2)  # Returns all elements that are in this(set1) set but not the others
print(my_set)

my_set = set2.difference(set1)  # # Returns all elements that are in this(set2) set but not the others
print(my_set)

set1 = {2, 3, 4, 5, 7, 8}
set2 = {1, 2, 4}
my_set = set2.issubset(set1)  # Report whether another set contains this set. returns True/False
print(my_set)
