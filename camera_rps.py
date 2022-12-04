import random
import cv2
from keras.models import load_model
import numpy as np
import time 

def timer():
    counter = 3
    while counter > 0:
        print(f'Show your hand in {counter}...')
        time.sleep(1)
        counter -= 1
        print('Show your hand!')
      
def get_prediction ():
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        print(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



        # Press q to close the window
        print(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
                
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
        return prediction


def get_computer_choice():
    computer_choice = random.choice(["rock", "paper", "scissors"])
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