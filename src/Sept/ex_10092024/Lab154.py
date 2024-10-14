# try , except and finally
# file
import os

try:
    file = open('testdata.txt', 'r')  # FileNotFoundError: [Errno 2] No such file or directory: 'example.txt'
    print(file.read())

except FileNotFoundError as fnfe:
    print("File Not found Error. Fix the path or create a file")

finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)
