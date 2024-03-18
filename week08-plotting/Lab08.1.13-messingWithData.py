# This program prints a bar chart between height and age of students
# Author: Filipe Carvalho

# here I added import pandas

import numpy as np
import matplotlib.pyplot as plt



minAge = 16
maxAge = 65
numberOfEntries = 100

minHeight = 150
maxHeight = 210


# make the array of occurrences
np.random.seed(1) 
randAge = np.random.randint (minAge, maxAge, numberOfEntries)
randHeight = np.random.randint (minHeight, maxHeight, numberOfEntries)


# we can now put this into a bar chart
plt.bar(randAge,randHeight, label="Age x Height")
plt.show()
