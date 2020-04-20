num = []
while True:
    num.append(int(input('Enter a number: ')))
    r = str(input('Continue? [Y/N] ')).upper().strip()[0]
    if r in 'Nn':
        break
num.sort(reverse=True)
print('-=' * 30)
print(f'You entered {len(num)} numbers.')
print(f'The values in descending order is {num}.')
if 5 in num:
    print('The number 5 is in the list!')
else:
    print('The number 5 is NOT in the list.')
