n = int(input('First number: '))
p = int(input('Pace: '))
n0 = n
c = 1
while c <= 10:
    print('{} -> '.format(n0), end='')
    n0 += p
    c += 1
print('End')
