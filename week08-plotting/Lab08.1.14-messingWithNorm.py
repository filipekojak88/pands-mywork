# This program prints a bar chart of the normal distribution of heights in certain population.
# Author: Filipe Carvalho

# here I added import pandas

import numpy as np
import matplotlib.pyplot as plt
import statistics


minAge = 16
maxAge = 65
numberOfEntries = 100

minHeight = 150
maxHeight = 210


# make the array of occurrences
np.random.seed(1) 
randAge = abs(np.random.randint (minAge, maxAge, numberOfEntries))
randHeight = abs(np.random.randint(minHeight, maxHeight, numberOfEntries))
average = sum(randAge)/numberOfEntries
normalRandAge = np.random.normal(loc=average, scale = 1.33, size = 100)

# we can now put this into a bar chart
plt.bar(normalRandAge, label="Age")
plt.show()