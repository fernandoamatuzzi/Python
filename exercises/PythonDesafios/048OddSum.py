sum = 0
count = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        count += 1
        sum += c
print('The sum of all {} values is {}.'.format(count, sum))
