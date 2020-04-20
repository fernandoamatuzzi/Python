num = list()
while True:
    n = (int(input('Enter a number: ')))
    if n not in num:
        num.append(n)
        print('Value added with success!')
    else:
        print('Duplicated value. Not added.')
    r = str(input('Continue? [Y/N] ')).upper().strip()[0]
    if r in 'Nn':
        break
print('-=' * 30)
num.sort()
print(f'You entered {num}')
