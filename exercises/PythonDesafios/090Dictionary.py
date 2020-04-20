student = {}
student['name'] = str(input('Name: '))
student['average'] = float(input(f'Average of {student["name"]}: '))
if student['average'] >= 7:
    student['situation'] = 'Approved'
elif 5 <= student['average'] < 7:
    student['situation'] = 'Recovery'
else:
    student['situation'] = 'Reproved'
print('-=' * 30)
for k, v in student.items():
    print(f'{k} is equals to {v}')
