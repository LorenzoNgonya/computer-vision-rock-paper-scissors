import random

def get_computer_choice():
    computer_choice = random.choice(["rock", "paper", "scissors"])
    #
    return computer_choice

def get_user_choice():
    user_choice =  input("What's your choice? (rock, paper, scissors)").lower()
    print(user_choice)
    return user_choice

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print ("It's a draw!")
        return print (" You both chose {}.".format(user_choice))
    if user_choice == "rock" and computer_choice == "scissors":
        print("You won!")
        return print ("computer chose {}.:".format (computer_choice))
    if user_choice == "paper" and computer_choice == "rock":
        print("You won!")
        return print ("computer chose {}.:".format (computer_choice))
    if user_choice == "scissors" and computer_choice == "paper":
        print("You won!")
        return print ("computer chose {}.:".format (computer_choice))
    else:
        print("You lost")
        return print ("computer chose {}.:".format (computer_choice))

def play():
    while True:
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()
        get_winner(user_choice, computer_choice)

        # Ask the user if they want to play again
        again = input("Do you want to play again? (y/n) ").lower()
        if again != "y":
            break

play()