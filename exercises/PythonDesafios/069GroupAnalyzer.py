tot18 = totMen = totW20 = 0
while True:
    print('-' * 30)
    print('{:^30}'.format('PEOPLE REGISTRATION'))
    print('-' * 30)
    age = int(input('Age: '))
    gender = ' '
    while gender not in 'MF':
        gender = str(input('Gender: [M/F] ')).upper().strip()[0]
    if age >= 18:
        tot18 += 1
    if gender == 'M':
        totMen += 1
    if gender == 'F' and age < 20:
        totW20 += 1
    print('-' * 30)
    option = ' '
    while option not in 'YN':
        option = str(input('Want to continue registering? [Y/N] ')).upper().strip()[0]
    if option == 'N':
        break
print(f'The total amount of people over 18 years old is {tot18}.')
print(f'The total amount of men registered is {totMen}.')
print(f'The total amount of women under 20 years old is {totW20}.')
