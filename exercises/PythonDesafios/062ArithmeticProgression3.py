n = int(input('First number: '))
p = int(input('Pace: '))
n0 = n
c = 1
total = 0
more = 10
while more != 0:
    total += more
    while c <= total:
        print('{} -> '.format(n0), end='')
        n0 += p
        c += 1
    print('Pause')
    more = int(input('How many terms you want to show more? '))
print('Progression ended with {} terms shown.'.format(total))
