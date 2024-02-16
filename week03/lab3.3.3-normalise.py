# This program reads a string
# and strips any leading or trailing spaces 
# also converts the string to lower case
# and output the length of the input and output strings
# author: Filipe Carvalho

rawString = input('please enter a string:')
normalisedString = rawString.strip().lower()

lengthOfRawString = len(rawString)
lengthOfNormalised = len(normalisedString)

print(f"That String normalised is: {normalisedString}")
print(f"We reduced the input string from {lengthOfRawString} to {lengthOfNormalised} characters")
