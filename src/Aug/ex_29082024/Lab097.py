# Tuple - Collection of Items
squares = [1, 4, 9, 16, 25]  # List is Mutable in nature (mutable means to change)

squares[3] = 64
print(squares)

# Tuple - Collection of Items
my_tuple = (1, 4, 3, 16, 25)
# my_tuple[3] = 64  # 'tuple' object does not support item assignment
print(my_tuple)  # immutable in nature

shopping_list_wife = ["bread", "paneer", "milk"]
shopping_list_wife[2] = "butter"
print(shopping_list_wife)

# Suppose you are working with Real world project
# 1. thetestingacademy.com, 2. sdet.live
my_tuple = ("tta.com", "sdet.live")

# Can convert list[] to tuple() and vice versa.
my_api_list = list(my_tuple)  # tuple() to list[]
print(my_api_list)

my_api_tuple = tuple(my_tuple)  # list[] to tuple()
print(my_api_tuple)

# Real case, where we Tuples
API_URLSs = ("https://sdet.live/python0x", "https://awesomeqa.com", "https://thetestingacademy.com")
print(API_URLSs[0])
print(API_URLSs[1])
