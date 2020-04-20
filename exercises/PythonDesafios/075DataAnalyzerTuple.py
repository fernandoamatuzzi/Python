num = (int(input('Enter a number: ')), int(input('Enter another number: ')),
       int(input('Enter one more number: ')), int(input('Enter the last number: ')))
print(f'You entered the numbers {num}.')
print(f'The number 9 appeared {num.count(9)} times.')
if 3 in num:
    print(f'The number 3 appeared in the position {num.index(3)+1}.')
else:
    print('The number 3 was not entered in any position.')
print(f'The even numbers are ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
