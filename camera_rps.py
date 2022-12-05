import random
import cv2
from keras.models import load_model
import numpy as np
import time 


list_choices = ["rock", "paper", "scissors"]

class CV_RPS:

    def __init__(self):
        self.computer_wins = 0
        self.user_wins = 0
        self.end = False
    
    def get_computer_choice(self):
        computer_choice = random.choice(list_choices)
        return computer_choice

    def get_prediction (self):
        model = load_model('keras_model.h5')
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        start = time.time()
        end_time = start + 4
        countdown = start + 3
        cap = cv2.VideoCapture(0)

        while time.time() < end_time:
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.imshow('frame', frame)
            # Press q to close the window
            print(prediction)

            while time.time() < countdown: # Initiating Countdown Timer
                print (f"Show your hand in... {int(end_time - time.time())}")
                break
            
            while countdown < time.time() < end_time:
                print ("Show your hand!")
                break
 
            time.sleep(1)
            counter -= 1
            print('Show your hand!')
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
            
        if prediction[0][0] > 0.5:
            return "Rock"
        elif prediction[0][1] > 0.5:
            return "Paper"
        elif prediction[0][2] > 0.5:
            return "Scissors"
        else:
            return "Nothing"
   
    def get_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            print ("It's a draw!")
            return print (" You both chose {}.".format(user_choice))
        if user_choice == "rock" and computer_choice == "scissors":
            self.user_wins += 1
            print("You won!")
            return print ("computer chose {}.:".format (computer_choice))
        if user_choice == "paper" and computer_choice == "rock":
            self.user_wins += 1
            print("You won!")
            return print ("computer chose {}.:".format (computer_choice))
        if user_choice == "scissors" and computer_choice == "paper":
            self.user_wins += 1
            print("You won!")
            return print ("computer chose {}.:".format (computer_choice))
        else:
            self.computer_wins += 1
            print("You lost")
            return print ("computer chose {}.:".format (computer_choice))

    def play(self):
        while not self.end:
            computer_choice = self.get_computer_choice(list_choices)
            user_choice = self.get_prediction()
            self.get_winner(user_choice, computer_choice)

            if self.computer_wins == 3:
                print('Game Over!\nComputer Wins!')
                self.end = True
            elif self.user_wins == 3:
                print('Game Over!\nYou Win!')
                self.end = True

game = CV_RPS(list_choices)
game.play()