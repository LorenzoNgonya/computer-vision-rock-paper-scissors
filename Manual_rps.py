
import random # imports random module 



def get_computer_choice():  #gets the computer choice randomly 
    computer_choice = random.choice (["rock", "paper", "scissors"])
    return get_computer_choice


def get_user_choice(): # gets the users choices 
    user_choice = input ("What's your choice?(rock, paper, scissors)")
    user_choice = user_choice.lower()
    return get_user_choice
    

def get_winner(get_computer_choice, get_user_choice):
    while True:
        if get_user_choice == "rock":
            if get_computer_choice == "scissors":
                print ("You won!")
        elif get_computer_choice == "paper":
                print ("You lost")
                
        
        if get_user_choice == "paper":
            if get_computer_choice == "rock":
                print ("You won!")
        elif get_computer_choice == "scissors":
                print ("You lost")
                
        
        if get_user_choice == "scissors":
            if get_computer_choice == "paper":
                print ("You won!")
        elif get_computer_choice == 'rock':
                print ("You lost")
        else:    
            if get_user_choice == get_computer_choice:
                print ("It is a tie!")
             
            
def play():
    get_computer_choice
    get_user_choice
    get_winner(get_user_choice, get_computer_choice)

play()