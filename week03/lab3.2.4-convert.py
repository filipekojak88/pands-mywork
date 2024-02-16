# This program takes a float amount of dollars 
# and returns that absolute amound in cents
# this is an extra activity
# author: Filipe Carvalho



amount = float(input("Please enter an amount:")) # Input in float
absolute = abs(amount) # Change the float to an absolute value



outcomes = int (absolute * 100) # Multiply to 100 and transform in interger
print(f'That amount in cent is: {outcomes}')
