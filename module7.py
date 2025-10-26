#create dictionary of all details as per requirements
courses = {
    'CSC101': {'room': '3004', 'instructor': 'Haynes', 'time': '8:00 a.m.'},
    'CSC102': {'room': '4501', 'instructor': 'Alvarado', 'time': '9:00 a.m.'},
    'CSC103': {'room': '6755', 'instructor': 'Rich', 'time': '10:00 a.m.'},
    'NET110': {'room': '1244', 'instructor': 'Burke', 'time': '11:00 a.m.'},
    'COM241': {'room': '1411', 'instructor': 'Lee', 'time': '1:00 p.m.'}
}

#ask user for course number
course = input('Enter a course number: ').upper()

#display course number information
if course in courses:
    print(f'{course} is held in Room Number: {courses[course]["room"]}, lead by {courses[course]["instructor"]}, and takes place at {courses[course]["time"]}')
else:
    print('Course not found.')