# This is an extra activity
# In this activity I have to fix the error in the message

# author: Filipe Carvalho

# Start: message = 'I have eaten ' + 99 + ' burritos.'
# Start: print (message)
# Question: Why does this expression cause an error? 
# Answer: Because 99 is an interger and not a string

# Question: How can you fix it?
# It seems that 99 was meant to be a string
# Answer: transform 99 value to a string



message = 'I have eaten ' + str(99)+ ' burritos'
print (message)


# Question: 7. Why is eggs a valid variable name while 100 is invalid?
# Response: Because Python has a rule which does not allow variable names to start with a number
# However, a variable can have a number as long as the first character is a letter

# Question: 8. What three functions can be used to get the integer, floating-point number, or string version of a value?
# Response: int(), float() and str()