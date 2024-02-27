# This program reads in a student name
# then it reads the modules 
# and each grade until
# the user press blank for module
# it saves the data in a dictionary
# the program prints out her data
# author: Filipe Carvalho

student = {'name': input('Enter student name: '),
           'modules': []
}
while True:
    courseName = input('Enter module name (blank to quit): ')
    if courseName == '':
        break
    else:
        grade = int(input('Enter grade for {}: '.format(courseName)))

    student['modules'].append({'courseName':courseName,'grade':grade})

print ('Student data:')
print ('Name:', student['name'])
print ('Modules:')
for module in student['modules']:
        print('- Course: {}'.format(module['courseName']))
        print('- Grade: {}'.format(module['grade']))
