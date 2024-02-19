# Modify the program guess2.py
# so the program tells the user
# if their guess is too high or too low
# using if statement inside the while loop
# author: Filipe Carvalho

numberToGuess = 20

guess = int(input("Please guess the number"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print ("too low")
    else: # I know i cant be equal or too low, so. it must be too high
        print ("too high")
    guess = int(input("Please guess again:"))

print ("Well done! Yes the number was ", numberToGuess)