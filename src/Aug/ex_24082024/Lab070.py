def sum_of_3_numbers(a=5, b=20, c=30):  # we can also pass default values in the def
    return a + b + c


# we can call function with multiple arguments or with NO arguments
result = sum_of_3_numbers(10, 20, 25)
result = sum_of_3_numbers(10, 20)
result = sum_of_3_numbers(5)
result = sum_of_3_numbers(a=24, c=34)
result = sum_of_3_numbers()
print(result)
