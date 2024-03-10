# This program allows a user to create new students and to view students
# This will be divided in some parts.
# author: Filipe Carvalho

# Part 1:
# This part has a function that prints out a menu of commands 
# we can perform such as add, view and quit.

# def displayMenu():
#    print("What would you like to do?")
#    print("\t(a) Add new students")
#    print("\t(v) View students")
#    print("\t(q) Quit")
#    choice = input("Type one letter (a/v/q):").strip()

#    return choice
# test the function
# choice = displayMenu()
# print(f'you chose { choice }')


# Part 2:
# This part keeps displaying the menu until the user picks "q"
# if the user chooses "a" then 
# the program calls a function called "doAdd()"
# if the user chooses "v" then
# the program calls a funciton called "doView()"
# def doAdd():
    # we fill this in later
#    print ("in adding")
# def doView():
    # we will this in later
#    print ("in viewing")

# main program
#choice = displayMenu()
#while (choice != 'q'):
    # we could do this with lambda functions
    # I am keeping this basic for the moment
#    if choice == 'a':
#        doAdd()
#    elif choice == 'v':
#        doView()
#    elif choice != 'q':
#        print ('\n\nplease select either a, v or q')
#    choice = displayMenu()
# Part 3:
# This part reads in the student's name
# reads in the module names and grades 
# creates a student dict
# prints out
# students=[]
# def readModules():
#    return[]
# def doAdd(students):
#    currentStudent = {}
#    currentStudent['name']=input('enter name :')
#    currentStudent['modules']=readModules()

#    students.append(currentStudent)

# test
# doAdd(students)
# doAdd(students)
# print(students)

# Part 4:
# This part reads modules until the user enters blank
# def readModules():
#    modules = []
#    moduleName = input ("\tEnter the first Module name (blank to quit):").strip()
  
#    while moduleName != "":
#        module = {}
#        module['name']=moduleName
        # I am not doing error handling
#        module['grade']=int(input('\t\tEnter grade:'))
#        modules.append(module)
        # now read the next module name
#        moduleName = input('\tEnter next module name (blank to quit):').strip()
#    return modules

# test
# doAdd(students)
# doAdd(students)
# print(students)




# Part 5: we put everything together
# the array we store everything in:
# order:
#   Part 1:
def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new students")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()

    return choice
#   Second half of part 3:
def doAdd(students):
    currentStudent = {}
    currentStudent['name']=input('enter name :')
    currentStudent['modules']=readModules()

    students.append(currentStudent)
#   Part 4:
def readModules():
    modules = []
    moduleName = input ("\tEnter the first Module name (blank to quit):").strip()
  
    while moduleName != "":
        module = {}
        module['name']=moduleName
        # I am not doing error handling
        module['grade']=int(input('\t\tEnter grade:'))
        modules.append(module)
        # now read the next module name
        moduleName = input('\tEnter next module name (blank to quit):').strip()
    return modules

#   This extra part:
# def doView (students):
    # we fill this in later
#    print (students)
# Part 6:
# This part is for the doView() function.
def displayModules(modules):
    print('\tName   \tGrade')
    for module in modules:
        print(f'\t{ module["name"]}   \t{module["grade"]}')

def doView(students):
    for currentStudent in students:
        print (currentStudent['name'])
        displayModules(currentStudent['modules'])
        
#   First half of part 3:
students=[]  

#   Second half of Part 2:
choice = displayMenu()
while (choice != 'q'):
    # we could do this with lambda functions
    # I am keeping this basic for the moment
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice != 'q':
        print ('\n\nplease select either a, v or q')
    choice = displayMenu()



    
