# This program put 10 random numbers into a queue(list)
# output all the values in the queue 
# takes the numbers from the queue one at a time
# print it and the current numbers still in the queue
# Author: Filipe Carvalho

import random
randomNo = []
CountNo = 10
rangeTo = 1000

for n in range (0,CountNo):
    randomNo.append(random.randint(0,rangeTo))

print(f'queue is {randomNo}')

while len(randomNo) != 0:
    currentNo = randomNo.pop(0)
    print (f'current Number is {currentNo} and the queue is {randomNo} ')

print ('the queue is now empty')