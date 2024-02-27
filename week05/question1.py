# This program determines the type of variables for different data
# Author: Filipe Carvalho

numberOfQuestions = 5
averageAge = 23.4
debugMode = True
name = "joe"
ages = []
months = ('Jan', 'Feb', 'Mar')
book = {}
stuff = [ 12 , 'Fred', False, {}]
someone = dict(firstname = "joe")
me = {
"firstName" : "Andrew",
"teaching" : [{
"courseName" : "programming",
"semester" : 1
},{
"courseName" : "Data Representation",
"semester" : 2
}
]
}
print (type(numberOfQuestions))
print (type(averageAge))
print (type(debugMode))
print (type(name))
print (type(ages))
print (type(months))
print (type(months[1]))
print (type(book))
print (type(stuff))
print (type(stuff[2]))
print (type(someone))
print (type(someone['firstname']))
print (type(me))
print (type(me['teaching']))
print (type(me['teaching'][0]['semester']))
print (type(me["teaching"][0]["coursename"]))

# Questions
# What are the variable types of the following variables in the code above
# a. numberOfQuestions = interger
# b. averageAge = float
# c. debugMode = Boolean
# d. name = String
# e. ages = list
# f. months = tuple
# g. months[1] = string
# h. book = dictionary
# i. stuff = list
# j. stuff[2] = Boolean
# k. someone = dictionary
# l. someone["firstname"] = string
# m. me = dictionary
# n. me["teaching"] = list
# o. me["teaching"][0]["semester"] = interger
# p is a trick question look at it carefully
# p. me["teaching"][0]["coursename"] = SyntaxError
