
import random # imports random modulde 

def get_computer_choice():  #gets the computer choice randomly 
    computer_choice = random.choice (['r', 'p' ,'s'])
    print (computer_choice)


def get_user_choice(): # gets the users choices 
    user_choice = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    user_choice = user_choice.lower()
    print (user_choice)

def get_winner(get_computer_choice, get_user_choice):
    while True:
        if get_user_choice == 'r':
            if get_computer_choice == 's':
                print ("You won!")
        elif get_computer_choice == 'p':
                print ("You lost")
    
        if get_user_choice == 'p':
            if get_computer_choice == 'r':
                print ("You won!")
        elif get_computer_choice == 's':
                print ("You lost")
        
        if get_user_choice == 's':
            if get_computer_choice == 'p':
                print ("You won!")
        elif get_computer_choice == 'r':
                print ("You lost")
        else:
            if get_computer_choice == get_user_choice:
                print ("It is a tie!")
                break
def play():
    get_computer_choice()
    get_user_choice()
    get_winner()