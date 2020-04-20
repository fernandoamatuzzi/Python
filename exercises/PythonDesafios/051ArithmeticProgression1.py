n = int(input('First number: '))
p = int(input('Pace: '))
dec = n + (10 - 1) * p
for c in range(n, dec + p, p):
    print('{}'.format(c), end=' -> ')
print('END')
