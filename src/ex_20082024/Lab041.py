# ✅ Grade Calculator:
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

score = int(input("enter your score\n"))
if score >= 90 and score <= 100:  # In this case Python suggests like this 90 <= score <= 100
    print("your Grade is ", "A")
elif score >= 80 and score <= 89:  # Its called "simplified chained comparison" 80 <= score <= 89
    print("your Grade is ", "B")
elif score >= 70 and score <= 79:
    print("your Grade is ", "C")
elif score >= 60 and score <= 69:
    print("your Grade is ", "D")
elif score >= 0 and score <= 59:
    print("your Grade is ", "F")
