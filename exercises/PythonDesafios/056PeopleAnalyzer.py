sumage = 0
average = 0
olderage = 0
oldername = ''
totwoman20 = 0
for people in range(1, 5):
    print('------- person {} -------'.format(people))
    name = str(input('Name: ')).strip()
    age = int(input('Age: '))
    gender = str(input('Gender (M/F): ')).strip()
    sumage += age
    if people == 1 and gender in 'Mm':
        olderage = age
        oldername = name
    if gender in 'Mm' and age > olderage:
        olderage = age
        oldername = name
    if gender in 'Ff' and age < 20:
        totwoman20 += 1
average = sumage / 4
print('The average age of the group is {} years old.'.format(average))
print('The older man is {} years old and his name is {}.'.format(olderage, oldername))
print('In total there are {} women under 20 years old.'.format(totwoman20))
