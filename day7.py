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
total_attempts = 0

while True:
    system_data = random.randint(i, j)
    count = 0

    print(f"\nGuess the number between {i} and {j}")
    print(f"You have {max_attempt} attempts.")

    while count < max_attempt:
        print("\nAttempts remaining:", max_attempt - count)

        try:
            user_data = int(input("Guess number: "))

            if user_data < i or user_data > j:
                print(f"Please enter a number between {i} and {j}.")
                continue

        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        count += 1
        total_attempts += 1

        if user_data == system_data:
            print(f"You guessed it right in {count} attempt(s)!")
            break

        if user_data < system_data:
            print("Please try a higher number.")
        else:
            print("Please try a lower number.")

    else:
        print("\nNo attempts remaining.")
        print("The correct number was:", system_data)

    while True:
        again = input("\nDo you want to play again (Yes/No): ").strip().lower()

        if again in ("yes", "y"):
            break
        elif again in ("no", "n"):
            print("\nThanks for playing!")
            print("Total attempts across all games:", total_attempts)
            exit()
        else:
            print("Please enter Yes or No.")

    # If the user chose "yes", the outer loop starts a new game.
        