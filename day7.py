# loop practice

import random

# while True:
#     print("Hello world")
#     break

# i = 0
# while i <= 10:
#     print(i)
#     i+=1

# system_data = str(random.randint(1, 10))
# count = 0
# while True:
#     user_data = input("Enter number from 1 to 10: ")
#     count += 1
#     if user_data == system_data:
#         print("Correct")
#         print("user_data is : ", user_data)
#         print("system_data is : ", system_data)
#         break
#     else:
#         print("wrong")

# print("Your total attempt is: ", count)

# import random

# i = 1
# j = 10

# attempt = 5
# count = 0
# system_data = random.randint(i, j)

# while True:
#     print("Attempt remaining:", attempt)

#     user_data = int(input("Guess number: "))

#     count += 1

#     if user_data == system_data:
#         print("You guessed it right!")

#         again = input("Do you want to play again (Yes/No): ")

#         if again.lower() == "yes":
#             system_data = random.randint(i, j)
#             attempt = 5
#             count = 0          # optional
#             continue
#         else:
#             break

#     attempt -= 1

#     if attempt == 0:
#         print("No attempts remaining.")
        
#         again = input("Do you want to play again (Yes/No): ")

#         if again.lower() == "yes":
#             system_data = random.randint(i, j)
#             attempt = 5
#             count = 0          # optional
#             continue
#         else:
#             break

#     if user_data < system_data:
#         print("Please try a higher number.")
#     else:
#         print("Please try a lower number.")

# print("Total attempts:", count)
# print("Random number was:", system_data)


import random

i = 1
j = 10

max_attempt = 5
count = 0
system_data = random.randint(i, j)

while True:
    print("Attempt remaining:", max_attempt - count)

    user_data = int(input("Guess number: "))
    count += 1

    if user_data == system_data:
        print("You guessed it right!")

        again = input("Do you want to play again (Yes/No): ")

        if again.lower() == "yes":
            system_data = random.randint(i, j)
            count = 0
            continue
        else:
            break

    if count >= max_attempt:
        print("No attempts remaining.")

        again = input("Do you want to play again (Yes/No): ")

        if again.lower() == "yes":
            system_data = random.randint(i, j)
            count = 0
            continue
        else:
            break

    if user_data < system_data:
        print("Please try a higher number.")
    else:
        print("Please try a lower number.")

print("Total attempts:", count)
print("Random number was:", system_data)
        