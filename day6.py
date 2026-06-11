import random


# loop :for : finite, while : infinite, continue, break, nested loop
# for is used in list, dictionay, string, range, tuple

# in list
# for i in [1,2,3,4,5]:
#     print(i,end=" ")

# a = {
#     "name":'sagar',
#     "id":12
# }

# # in dictionary for key
# print("\n")
# for i in a:
#     print(i)

# # for values
# print("\n")
# for i in a.values():
#     print(i)

# # for values
# print("\n")
# for i in a:
#     print(a[i])

# # for items
# print("\n")
# for i in a.items():
#     print(i)

# # for items
# print("\n")
# for i,j in a.items():
#     print(i,j)

# for i in [1,2,3,4,5,6]:
#     if i==4:
#         # break
#         continue
#     print(i)

# for i in range(1,11,1):
#     if(i%2==0):
#         print(i, "is : even")
#     else:
#         print(i, "is : odd")

# for i in range(1,10):
#     print(i)

# print("------------------------")

# for i in range(10):
#     print(i)

# print("------------------------")

# for i in range(10,20):
#     print(i)

# print("------------------------")


# for i in range(10,1,-1):
#     print(i)

# number = int(input("Enter the value: "))
# for i in range(1,11):
#     a = number*i
#     print(f"{number} X {i} = {number*i}")



# for i in [1,2,3]:
#     for j in [4,5,6]:
#         print(i,j)
#     print("==================")



# print(random.random())

# data = [5,6,7,1,2,"hello","sagar"]
# print(random.choice(data))

# print(random.randint(10,20))

system_data = random.randint(1,10)
for i in range(1,6):
    user_data = int(input("Enter number from 1 to 10: "))
    if(user_data == system_data):
        print("Correct")
        print("user_data is : ",user_data)
        print("system_data is : ",system_data)
        break
    else:
        print("wrong")


