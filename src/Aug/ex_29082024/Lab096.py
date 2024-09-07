squares = [1, 4, 9, 16, 25]

# squares = [1, 4, 9, 16, 25, "Pramod"]  #  not supported between instances of 'str' and 'int'
# squares.sort(reverse=False) # Sort the list in descending order and return None.
squares.sort(reverse=True)  # Sort the list in ascending order and return None.
print(squares)

# pop: Remove and return item at index (default last).
print(squares.pop())
print(squares)