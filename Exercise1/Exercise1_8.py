# File name:    Exercise1_8.py
# Author:       Eerik Vainio
# Description:  A simple game of rock, paper, scissors.

import random

user_choice = cpu_choice = ""
user_input = "y"

# Main game loop. Check initially if the user wants to continue playing.
while(True):
    if(user_input.casefold() != "y"):
        break
    else:
        # Ask for the user's choice, break only if the input is correct.
        while(True):
            user_choice = input("Choose rock, paper or scissors: ").casefold()

            if(user_choice in ('rock', 'paper', 'scissors')):
                break
            else:
                print(f'"{user_choice}" is not a valid choice.')

        # Choose a random choice for the computer.
        match random.randint(0, 2):
            case 0:
                cpu_choice = "rock"
            case 1:
                cpu_choice = "paper"
            case 2:
                cpu_choice = "scissors"

        print(f"Player's choice: {user_choice}")
        print(f"Computer's choice: {cpu_choice}")

        # Check each possible combination, and output the result accordingly.
        match user_choice:
            case "rock":
                match cpu_choice:
                    case "rock":
                        print("It's a draw.")
                    case "paper":
                        print("Computer won!")
                    case "scissors":
                        print("Player won!")
            case "paper":
                match cpu_choice:
                    case "rock":
                        print("Player won!")
                    case "paper":
                        print("It's a draw.")
                    case "scissors":
                        print("Computer won!")
            case "scissors":
                match cpu_choice:
                    case "rock":
                        print("Computer won!")
                    case "paper":
                        print("Player won!")
                    case "scissors":
                        print("It's a draw.")

        user_input = input("Input 'Y' to play again: ")

