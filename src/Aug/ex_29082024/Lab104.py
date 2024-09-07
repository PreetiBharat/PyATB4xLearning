# Dictionary/Dict
# key - value pair - {}

student_info = {
    "name": "Preeti",
    "Age": 67,
    # "Age": 68,  # if duplicates, then it will consider the latest key- value
    "address": "KA"
}

print(student_info)
print(student_info["name"])
print(student_info["Age"])
print(student_info["address"])

student_info["Age"] = 100  # Can reassignment value
print(student_info)

student_infor1 = {
    "name": "Pramod",
    # "age": 65,
    "age": 67,
    "address": {
        "home_address": "ND",
        "office_address": "KA"
    }
}

student_infor2 = {
    "name": "Amit",
    # "age": 65,
    "age": 69,
    "address": {
        "home_address": "GOA",
        "office_address": "KA"
    }
}

student_list = [student_infor1, student_infor2]
print(student_list)
