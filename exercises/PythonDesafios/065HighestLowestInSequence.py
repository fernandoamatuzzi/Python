num = c = sum = 0
option = 'Y'
while option in 'Y':
    num = int(input('Enter a number: '))
    option = str(input('Do you want to enter a new number? [Y/N] ')).upper().strip()[0]
    sum += num
    c += 1
    if c == 1:
        higher = lower = num
    else:
        if num > higher:
            higher = num
        if num < lower:
            lower = num
average = sum / c
print('You entered {} numbers and the average between them is {:.2f}.'.format(c, average))
print('The higher number is {} and the lower number is {}.'.format(higher, lower))
