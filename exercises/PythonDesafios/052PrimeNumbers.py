n = int(input('Enter a number: '))
t = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\33[33m', end=' ')
        t += 1
    else:
        print('\33[31m', end=' ')
    print('{}'.format(c), end='')
print('\n\33[mThe number {} was divisible {} times.'.format(n, t))
if t == 2:
    print('And because of that, it \33[4mIS PRIME!')
else:
    print('And because of that it is \33[4mNOT PRIME!')
