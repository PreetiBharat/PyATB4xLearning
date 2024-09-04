# escape sequence

print("Hello world")  # \n new line
print("Hello\nWorld")  # \n New line
print("Hello\bworld")  # \b backspace
print("Hello\tWorld")  # \t tab line

# Concept of Raw string "r"
dir = r'C\Pramod\n.txt'  # \n in this taking to new line. To fix this we should use "r"(means raw)
print(dir)
dir2 = r"C\Preeti\n.txt"  # \n in this taking to new line. To fix this we should use "r"(means raw)
print(dir2)

name = r'Preeti\s shop'  # use of single quotes ' ' are not preferred in Python. Its good practice to use " "
print(name)
