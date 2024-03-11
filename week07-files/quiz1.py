# author: Filipe Carvalho
# Quiz:
# 1.
# a. Look at the program below, if the file test-a.txt does not exist. What will
# happen when the program runs?
# Response: A error message will be displayed 
# as the file test-a.txt does not exist.

# the with statement will automatically close the file
# when it is finished with it
# with open("test-a.txt") as f:
#    data = f.read()
#    print (data)
# the old way of doing this is
# f = open ("test1.txt")
# data = f.read()
# print(data)
# f.close()
    

# b. Look at the program below, if the file test-b.txt does not exist, what 
# will be outputted to the console when this program is run?
# Response: It will output the number of characters 7 and 13
# c. What will the contents of the file test-b.txt be when this program is run?
# Response: The contents will be two lines with the first one
# being "another line" and the second one empty.
    
# the with statement will automatically close the file
# when it is finished with it
# with open("test-b.txt", "w") as f:
#     data = f.write("test b\n") # returns the number of chars written
#     print (data)
# with open("test-b.txt", "w") as f2: # open file again
#     data = f2.write("another line\n")
#     print (data)


# d. Look at the modified program below, 
# what will the contents of the file be
# after this program is run?
# The contents will be three lines with the first one
# being "test d", second line is "another line",
# and third line is empty.


# The with statement will automatically close the file
# when it is finished with it
with open("test-d.txt", "w") as f:
    data = f.write("test d\n") 
    # returns the number of chars written
    print (data)
with open("test-d.txt", "a") as f2: # open file again
    data = f2.write("another line\n")
    print (data)