# This program generates randomly salaries and ages within a range and plot that in a scatterplot
# added a line in this plot with y=x^2 in a different color
# Author: Filipe Carvalho


import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

# this is so that the "random" numbers are the same each time to make it easier to debug.
np.random.seed(1) 
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
# I prefer putting the absolute values into variables taht are set at the top.
ages = np.random.randint(low=21, high=65, size = numberOfEntries) 




plt.scatter(ages, salaries)    
# plt.show  - if you do this the program will halt here until the plot is closed

# add x squared
xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints # multiply each entry by itself

plt.plot(xpoints, ypoints, color='r')
plt.show() # see how the axis have changed
