# This program reads a number and keeps asking for a number until -1 is input.
# author: Filipe Carvalho

number = str(input("enter an integer:"))

while number != '-1':
    print (f"{number} is not -1")
    number = input ("Please enter -1:")
print (f"You finally chosen the correct number: {number}")
