# This program creates a new array to the salaries from Lab08.1.2-salary.py adding 5000 to each salary in the list.
# Author: Filipe Carvalho

import numpy as np

# it is a good idea to have your absolute values set into variables at the beginning of your program
minSalary = 20000
maxSalary = 80000
numberOfEntries = 10
np.random.seed(1) # this is so that the "random" numbers are the same each time to make it easier to debug.
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
salariesPlus = salaries + 5000 # this will add 5000 to each value


print (salaries)
print (salariesPlus)