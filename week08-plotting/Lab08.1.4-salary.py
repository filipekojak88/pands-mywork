# This program add a new array of data multiplying by 1.05 each item in the list of salaries generated in Lab08.1.3-salary.py.
# Author: Filipe Carvalho

import numpy as np

# it is a good idea to have your absolute values set into variables at the beginning of your program
minSalary = 20000
maxSalary = 80000
numberOfEntries = 10
np.random.seed(1) # this is so that the "random" numbers are the same each time to make it easier to debug.
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
salariesPlus = salaries + 5000 # this will add 5000 to each value
# you can also multiply
salariesMult = salaries * 1.05 # add 5% by multiplying by 1.05


print (salaries)
print (salariesPlus)
print (salariesMult)

# This is a float array, here I conver it to an int array (it does a floor)
newSalaries = salariesMult.astype(int)
print (newSalaries)