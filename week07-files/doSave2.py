# This program uses the basis of the program
# lab6.1.2_student1.py and doSave.py 
# and add savedict() function into it
# author: Filipe Carvalho

import json
# the array we store everything in 
students= []
FILENAME="students.json"
def writeDict(obj):
    with open(FILENAME, 'wt') as f:
        json.dump(obj,f)

def displayMenu():
    print("what would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(s) Save students")
    print("\t(q) Quit")
    choice = input("type one letter (a/v/s/q):").strip()

    return choice

def doAdd():
    currentStudent = {}
    currentStudent["name"]=input("Enter name :")
    currentStudent["modules"]= readModules()
    students.append(currentStudent)

def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit) :").strip()
    
    while moduleName != "":
        module = {}
        module["name"]= moduleName
        # I am not doing error handling
        module["grade"]=int(input("\t\tEnter grade:"))
        modules.append(module)
        # now read the next module name
        moduleName = input("\tEnter next module name (blank to quit) :").strip()

    return modules

def displayModules(modules):
    print ("\tName   \tGrade")
    for module in modules:
        print(f"\t{module['name']}  \t{module['grade']}" )

def doView():
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"]); 

def doSave():
    writeDict(students)
    print("students saved")

#main program
choice = displayMenu()
while(choice != 'q'):
    # we could do this with lamda functions
    # I am keeping this basic for the moment
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice == 's':
        doSave()
    elif choice !='q':
        print("\n\nPlease select either a,v,s or q")
    choice=displayMenu()

    # Adding the savedic() function into the program above