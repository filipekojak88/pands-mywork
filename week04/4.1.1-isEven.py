# This program reads a number and output if number is even or odd.
# author: Filipe Carvalho

number = int(input("enter an integer:"))
if (number%2) == 0:
    print (f'{number} is an even number')
else:
    print (f'{number} is an odd number')