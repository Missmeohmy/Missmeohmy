#This program will generate a random number between 1 and 9. It will ask the user to guess the number then tell the user if their guess was too high, low or perfect. 

import random

def num():
    count = 0
    a = random.randint(1,9)
    while a != 0:
        guess = input("What is your guess? Type '0' to quit: ")
        guess = int(guess)
    
        if guess == 0:
            print("Sayonara!")
            quit()
        elif guess == a:
            print("Well look at the big brain on Brad?!")
            print("Do you want to play again?")
            replay = input("Type 'Yes'or 'Exit': ").lower()
            if replay == 'yes':
                num()  
            else:
                print("Sayonara!")
                quit()
        
        elif guess <= a:
            print("Too low amigo! Try another!")
        
        else:
            print("Way too high compadre! Guess again!")
        
      
        
print("Welcome to the guessing game! Try to guess what number is selected between 1-9.")
num()
