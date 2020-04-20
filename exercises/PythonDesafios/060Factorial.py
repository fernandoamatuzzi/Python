'''from math import factorial
n = int(input('Enter a number to get its factorial: '))
f = factorial(n)
print('The factorial of {} is {}.'.format(n, f))'''
'''n = int(input('Enter a number to get its factorial: '))
c = n
f = 1
print('Calculating {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))'''
n = int(input('Enter a number to get its factorial: '))
c = n
f = 1
print('Calculating {}! = '.format(n), end='')
for c in range(n, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
