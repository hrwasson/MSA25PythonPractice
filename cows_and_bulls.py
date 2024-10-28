'''
Cows and Bulls

Create a program to play the game "cows and bulls." This is how the game works.

    Randomly generate a 4-digit number in the range 0000 to 9999.
    Ask the user to guess the target number.
    For every digit the user guesses correctly, they receive a cow.
    For every digit the user guesses incorrectly, they receive a bull.
    Count how many guesses it takes for them to guess the target number. 

'''

import numpy as np
import random

# initialize the number of cows, bulls, and guesses to proper starting values 

random.seed(123)
cows = 0 
bulls = 0
guess_count = 0 


random_number = str(np.random.randint(low=1000,high=9999))

while cows != 4: 
    guess = input("Guess a number between 1000 and 9999: ")
    for digit in guess:
        if digit in random_number: 
            cows += 1
        if digit not in random_number: 
            bulls += 1
    guess_count += 1
    print("Guess Number:", guess_count, "- You have", cows, "cow(s) and ", bulls, "bull(s)")
    if cows == 4: 
        print('You won!')
        print(random_number)
        break
    cows = 0
    bulls = 0
    








