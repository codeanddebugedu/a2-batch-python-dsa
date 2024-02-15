"""
Rock Paper Scissors

computer_choice = rock/paper/scissors

user_choice = input() rock/paper/scissors

if
elif
elif


You won
You lost, the computer choose rock/paper/scissors
You tied
"""

import random

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
user_choice = input("Enter rock/paper/scissors = ")

# IF-ELIF-ELIF

if user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
    print("INVALID")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You won")
elif user_choice == "paper" and computer_choice == "rock":
    print("You won")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You won")
elif user_choice == computer_choice:
    print("You tied")
else:
    print(f"You lost, computer choose {computer_choice}")
