# Modify the program guess2.py
# to generate a random number 
# between 0 and 100 to guess

# author: Filipe Carvalho

import random         # import random

numberToGuess = random.randint (0,100)      # add the radint() method and define the range


guess = int(input("Please guess the number"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print ("too low")
    else: # I know i cant be equal or too low, so. it must be too high
        print ("too high")
    guess = int(input("Please guess again:"))

print ("Well done! Yes the number was ", numberToGuess)