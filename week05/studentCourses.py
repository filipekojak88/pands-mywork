# This program stores a student name
# a list of her courses and grades in a dictionary
# the program prints out her data
# author: Filipe Carvalho

student = {'name':'Mary',
           'modules': [
               {
                   'courseName':'Programming',
                   'grade': 45
               },
               {
                   'courseName':'History',
                   'grade': 99
               }
        ]
}
print ('Student: {}'.format(student['name']))
for module in student ['modules']:
    print('\t {} \t: {}'.format(module['courseName'], module['grade']))
