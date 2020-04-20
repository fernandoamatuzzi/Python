values = []
even = []
odd = []
while True:
    values.append(int(input('Enter a number: ')))
    r = str(input('Continue? [Y/N] ')).upper().strip()[0]
    if r in 'N':
        break
for i, v in enumerate(values):
    if v % 2 == 0:
        even.append(v)
    else:
        odd.append(v)
print('-=' * 30)
print(f'The full list is {values}')
print(f'The even list is {even}')
print(f'The odd list is {odd}')
