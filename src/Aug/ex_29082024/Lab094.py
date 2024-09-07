# List
# List - Collection of Items( Duplicate is allowed)
my_list = [1, 2, 3]  # Same type of data (int)
# my_list2 = [1, True, "Pramod", 12.34]

print(my_list)
print(len(my_list))

print(my_list[0])
print(my_list[2])
# print(my_list[10])  # list index out of range

# you can change the value by reassigning it
my_list[0] = "Preeti"
my_list[1] = "Bharat"
my_list[2] = "Chougule"
# my_list[10] = "Chougule1"  # list assignment index out of range
print(my_list)

# Indexing
print("Element at the index 0| ", my_list[0])
print("Element at the index 1| ", my_list[1])
print("Element at the index 2| ", my_list[2])


# for element in my_list:
#     print(my_list)

for i in range(1, 10):
    print(i)  # [1,2,3,4,5,6,7,8,9]

# range(1,10,1) -> list -> [1,2,3,4,5,6,7,8,9]

print("_______________________")
my_list = [1, 2, 3]

# append(): If you want to add only item at the end of the list use this.
my_list.append(4)
my_list.append(5)  # Append object to the end of the list.
print(my_list)
print("___________________________")

# extend(): If you want to add more than one item at the end of the list use this.
my_list.extend([6, 7, 8])
my_list.extend([9])
my_list.extend(["Preeti"])
print(my_list)
print("_______________________")

# insert()
my_list.insert(10, "Chougule")  # you can insert value at any index
print(my_list)

print(len(my_list))
print("_______________________")

# replace()
my_list[1] = "Swara"  # to replace value from list reassign the value to the mentioned index.
print(my_list)
print("_______________________")

# insert()
my_list.insert(0, 0)
print(my_list)
my_list.insert(-2, "Bharat")  # inserts in reverse way. ex:-5,-4,-3,-2,-1,0
print(my_list)
print("_______________________")

# remove()
my_list.remove(3)
print(my_list)
print("_______________________")

# copy list()
my_copy_list = my_list.copy()
print(my_copy_list)
print("_______________________")

# reverse()
my_copy_list.reverse()
print(my_copy_list)
print("_______________________")

# clear()
my_list.clear()
print(my_list)
print(my_copy_list)
print("_______________________")

my_copy_list.remove("Swara")
my_copy_list.remove("Bharat")
my_copy_list.remove("Preeti")
my_copy_list.remove("Chougule")

# sort()
my_copy_list.sort()  # Sorting is not supported between instances of 'str' and 'int'
my_copy_list.sort(reverse=False)  # Sort the list in ascending order and return None.
print(my_copy_list)
print("_______________________")


# reverse
my_copy_list.reverse()
print(my_copy_list)
