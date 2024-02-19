# This program prompts the user to guess a number
# it keeps prompting the user to guess 
# until the right number is typed in
# author: Filipe Carvalho

numberToGuess = 20

guess = int(input("Please guess the number"))
while guess != numberToGuess:
    print ("Wrong")
    guess = int(input("Please guess again:"))

print ("Well done! Yes the number was ", numberToGuess)