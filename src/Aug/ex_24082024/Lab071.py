def sum_three(a=10, b=20, c=40):
    return a + b + c


result = sum_three()
print(result)

result1 = sum_three(12, 22)
print(result1)

result1 = sum_three(b=22, c=22)
print(result1)

result2 = sum_three(12, 22, 25)
print(result2)

result3 = sum_three(b=20, c=30, a=15)
print(result3)
