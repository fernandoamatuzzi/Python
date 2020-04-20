print('FIBONACCI SEQUENCE')
print('=-=' * 10)
term = int(input('How many terms do you want to show? '))
n1 = 0
n2 = 1
print('~' * 30)
print('{} -> {}'.format(n1, n2), end='')
c = 3
while c <= term:
    n3 = n1 + n2
    print(' -> {}'.format(n3), end='')
    n1 = n2
    n2 = n3
    c += 1
print(' -> End')
print('~' * 30)
