student = []
while True:
    name = str(input('Name: '))
    grade1 = float(input('Grade 1: '))
    grade2 = float(input('Grade 2: '))
    average = (grade1 + grade2) / 2
    student.append([name, [grade1, grade2], average])
    resp = str(input('Continue? [Y/N] ')).upper().strip()[0]
    if resp in 'N':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NAME":<10}{"AVERAGE":>8}')
print('-' * 30)
for i, a in enumerate(student):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 30)
    opt = int(input('Show grades of what student? (999 to exit): '))
    if opt == 999:
        print('Ending...')
        break
    if opt <= len(student) - 1:
        print(f'Grades of {student[opt][0]} are {student[opt][1]}')
print('Thank You!!')
