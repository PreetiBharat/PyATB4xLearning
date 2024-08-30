# Continue statement skips the current iteration of a loop and
# moves to the next iteration.

for number in range(1, 10):
    if number % 2 == 0:
        print(number)  # this prints even numbers
    else:
        continue

for number in range(1, 10):
    if number % 2 == 0:
        continue  # # this prints odd numbers
    else:
        print(number)

# | i  | Condition | O/P
# | 0  | 0%2 == 0 -> True | continue - skip No O/P
# | 1  | 1%2 == 0 -> False | 1
# | 2  | 1%2 == 0 -> True | continue - skip No O/P
# | 3  | 3%2 == 0 -> False | 3

# pass - can be used in the statement, functions, class and objects
