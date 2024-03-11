# author: Filipe Carvalho
# This program counts how many times it was run
# that exists



# This part is just to create the file using python and add 0 to it.
# writeNumber = 0 # the interger
# with open("count.txt", "w") as f:
#    data = f.write(str(writeNumber)) # returns the number of chars written
#    print (data)


# This part checks if the file exists.
# import os.path
# FILENAME = "count.txt"
# if not os.path.isfile(FILENAME):
#     print ("File does not exist")

# a) This function reads in a number from a file 
# that already exists 

# FILENAME = "count.txt"
# def readNumber():
#     try:
#         with open(FILENAME) as f:
#            number = int(f.read())
#            return number
#     except IOError:
        # this file will be created when we write back.
        # no file assumes first time running
        # ie 0 previous runs
#         return 0
# test it
# num = readNumber()
# print (num)


# b) This function takes in a number and overwrites a file
# with that number.

# def writeNumber(number):
#     with open(FILENAME, "wt") as f:
        # write takes a string so we need to convert
#         f.write(str(number))
# test it
# writeNumber(3)

# c) These functions count how many times 
# the program has been run.

FILENAME = "count.txt"
def readNumber():
    try:
        with open(FILENAME) as f:
            number = int(f.read())
            return number
    except IOError:
        # this file will be created when we write back.
        # no file assumes first time running
        # ie 0 previous runs
        return 0
def writeNumber(number):
    with open(FILENAME, "wt") as f:
        # write takes a string so we need to convert
        f.write(str(number))

# main
num = readNumber()
num += 1
print (f"we have run this program {num} times")
writeNumber(num)
