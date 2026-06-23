# file handling : read, write, append, read binary, write binary

# f = open("day1.py", "r")
# print(f.read())
# f.close()

# f = open("newfile.txt", "w")
# f.write("\nhello its me sagar")
# f.close()

# Write data
# with open("student.txt", "w") as file:
#     file.write("Name: Sagar\n")
#     file.write("Course: Python")

# # Read data
# with open("student.txt", "r") as file:
#     print(file.read())

# print("=================================")

# with open("student.txt", "r+") as file:
#     content = file.read()
#     print(content)

#     file.write("\nInstructor: Sudan")


# from datetime import datetime
# print(datetime.now())

# def error(file_name, message):
#     with open(file_name, "a") as f:
#          f.write(
#             f"{datetime.now().date()} | {type(message).__name__} | {message}\n"
#         )

# try:
#     a = 5 / 0

# except ZeroDivisionError as message:
#     error("err_division.txt", message)

# except NameError as message:
#     error("error_name.txt", message)

# except Exception as message:
#     error("err_general.txt", message)

# finally:
#     print("this is running")


import csv

count = -1

with open("data.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
        count += 1

print("Total rows:", count)
    

import csv

data = [
    ["dhiraj", "pokhara", 45],
    ["sagar", "kathmandu", 25]
]

with open("data.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
