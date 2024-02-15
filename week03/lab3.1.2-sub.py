# This program subtracts one number from another.
# input reads in a string so we need to convert it into an interger
# so we can perform mathematical operations
# author: Filipe Carvalho

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
answer = x - y
print ("{} minus {} is {}" .format(x, y, answer))
