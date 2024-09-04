# ✅ Grade Calculator: use of Simplified Chaining Format -> 90 <= score <= 100
# Write a program that calculates and displays the letter grade
# for a given numerical score (e.g., A, B, C, D, or F)
# based on the following grading scale:
#
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

# Logic Building Formula

# 1 -> User Inputs -> score or marks -> int
# 2 ->  O/p -> str -> A or B....

score = int(input("enter your score\n"))  # # Simplified Chaining Format -> 90 <= score <= 100
if 90 <= score <= 100:
    print("your Grade is ", "A")
elif 80 <= score <= 89:
    print("your Grade is ", "B")
elif 70 <= score <= 79:
    print("your Grade is ", "C")
elif 60 <= score <= 69:
    print("your Grade is ", "D")
elif 0 <= score <= 59:
    print("your Grade is ", "F")
