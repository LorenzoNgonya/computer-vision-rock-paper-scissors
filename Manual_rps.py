
import random # imports random module 



def get_computer_choice():  #gets the computer choice randomly 
    computer_choice = random.choice (["rock", "paper", "scissors"])
    return computer_choice


def get_user_choice(): # gets the users choices 
    user_choice = input ("What's your choice?(rock, paper, scissors)")
    user_choice = user_choice.lower()
    return user_choice
    

def get_winner(computer_choice, user_choice):
    #while True:
    if user_choice == computer_choice:
            print ("It is a tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print ("You won!")
    elif user_choice == "paper" and computer_choice == "rock":
        print ("You won!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print ("You won!")
    #else:
        print ("You lost")
    #break

        
       

            
            
def play():
    get_computer_choice()
    get_user_choice()
    get_winner(get_user_choice,get_computer_choice)

play()
