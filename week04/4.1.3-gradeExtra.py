# 3. In practice the percentages are rounded ie 69.5 gets rounded to 70 so is
# equal to a Distinction.
# How would you modify the program in 1 to deal with this?
# I see two ways.   

import math
percentage = round (float (input ('Enter the percentage: '))) # Answer: Way 1 - to add round to the float input / Way 2 - Change the type of variable to interger.
print (percentage)
if percentage < 0 or percentage > 100:
    print ('Please enter a number between 0 and 100')

elif percentage < 40:
    print ('Fail')
elif percentage < 50: 
    print ('Pass')
elif percentage < 60: 
    print ('Merit1')
elif percentage < 70: 
    print ('Merit2')
else: 
    print ('Distinction')