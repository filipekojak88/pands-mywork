# program that prints out a random number between 1 and 10
# author: Filipe Carvalho
# the program below was altered to request the user to input the first and second number
# so the program can display a random number between the two input numbers.

import random

x = int(input("Enter the first number of the range: ")) # type in the first number of the range
y = int(input("Enter the second number of the range: ")) # type in the second number of the range
number = random.randint(x,y)                             # run and bring a random betwee first and second number
print("{} is a random number between {} and {}".format( number, x, y))     # print the random number
