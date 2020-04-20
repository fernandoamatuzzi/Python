sum = 0
count = 0
for c in range(0, 6):
    n = int(input('Enter a number: '))
    if n % 2 == 0:
        sum += n
        count += 1
print('You informed {} even numbers and the sum is {}.'.format(count, sum))
