# This program reads in a student name
# then it reads the modules 
# and each grade until
# the user press blank for modules
# and reads the name until
# the user press blank for student name
# it saves the data in a dictionary
# the program prints out everybody's data
# author: Filipe Carvalho


student = {'name':[],'modules':[]} 
while True:
        name = input('Enter student name (blank to quit): ')
        if name == '':
            break
        else:
            modules_data = []
            while True:
                courseName = input('Enter module name (blank to quit): ')
                if courseName == '':
                    break
                else:
                    grade = int(input('Enter grade for {}: '.format(courseName)))
                    modules_data.append({'courseName':courseName,'grade':grade})
            student['name'].append(name)
            student['modules'].append(modules_data)
        
print ('Student data:')
for idx, student_name in enumerate(student['name']):
    print ('Name:', student_name)
    print ('Modules:')
    for module_data in student['modules'][idx]:
        print('- Course: {}'.format(module_data['courseName']))
        print('- Grade: {}'.format(module_data['grade']))
        
