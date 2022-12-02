
import random # imports random module 



def get_computer_choice():  #
    #"""function that gets the computer's choice randomly """
    computer_choice = random.choice (["rock", "paper", "scissors"])
    return computer_choice


def get_user_choice():
    #"""function that gets the user's choices"""
    user_choice =  input ("What's your choice?(rock, paper, scissors)")
    user_choice = user_choice.lower()
    return user_choice
    
    

def get_winner(computer_choice, user_choice):
    computer_choice = get_computer_choice
    user_choice = get_user_choice
    print (computer_choice)
    if user_choice == "rock" and computer_choice == "scissors":
        print ("You won!")
    elif user_choice == "paper" and computer_choice == "rock":
        print ("You won!")
        ###break
    elif user_choice == "scissors" and computer_choice == "paper":
        print ("You won!")
        #break
    else:
        print ("You lost")
  
    #break

 #if get_user_choice == "paper":
  ##          if get_computer_choice == "rock":
    #            print ("You won!")
     #   elif get_computer_choice == "scissors":
      #          print ("You lost")
       #         
        
         #   if get_computer_choice == "paper":
        #if get_user_choice == "scissors":
         #       print ("You won!")
        #elif get_computer_choice == 'rock':
         #       print ("You lost")
        #break

        
       
            
            
def play():
    get_computer_choice()
    get_user_choice()
    get_winner(get_user_choice,get_computer_choice)

play()
