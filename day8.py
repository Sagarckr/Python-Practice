# import random

# choices = ["rock", "paper", "scissors"]

# while True:
#     system_choice = random.choice(choices)
#     user_choice = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()

#     if user_choice == "quit":
#         print("Game ended.")
#         break

#     if user_choice not in choices:
#         print("Invalid choice! Try again.")
#         continue

#     print("Computer chose:", system_choice)

#     if user_choice == system_choice:
#         print("It's a tie!")

#     elif (
#         (user_choice == "rock" and system_choice == "scissors") or
#         (user_choice == "paper" and system_choice == "rock") or
#         (user_choice == "scissors" and system_choice == "paper")
#     ):
#         print("You win!")

#     else:
#         print("You lose!")


import random

choices = ["rock", "paper", "scissors"]

while True:
    user_score = 0
    computer_score = 0
    round_number = 1

    print("\n=== Rock Paper Scissors (Best of 5) ===")
    print("First to win 3 rounds wins the match.")
    print("Type 'quit' anytime to exit.\n")

    while user_score < 3 and computer_score < 3:
        print(f"Round {round_number}")
        print(f"Score -> You: {user_score} | Computer: {computer_score}")

        user_choice = input("Enter rock, paper, or scissors: ").strip().lower()

        if user_choice == "quit":
            print("\nGame ended.")
            exit()

        if user_choice not in choices:
            print("Invalid choice! Try again.\n")
            continue

        system_choice = random.choice(choices)

        print("Computer chose:", system_choice)

        if user_choice == system_choice:
            print("It's a tie!")

        elif (
            (user_choice == "rock" and system_choice == "scissors") or
            (user_choice == "paper" and system_choice == "rock") or
            (user_choice == "scissors" and system_choice == "paper")
        ):
            user_score += 1
            print("You win this round!")

        else:
            computer_score += 1
            print("Computer wins this round!")

        round_number += 1
        print()

    print("=== Match Result ===")
    print(f"Final Score -> You: {user_score} | Computer: {computer_score}")

    if user_score > computer_score:
        print("🎉 Congratulations! You won the match!")
    else:
        print("😢 Computer won the match!")

    again = input("\nDo you want to play again (Yes/No): ").strip().lower()

    if again not in ("yes", "y"):
        print("Thanks for playing!")
        break