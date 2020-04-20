num = c = sum = 0
num = int(input('Enter a number [999 to stop]: '))
while num != 999:
    sum += num
    c += 1
    num = int(input('Enter a number [999 to stop]: '))
print('You entered {} numbers and the sum of these numbers is {}.'.format(c, sum))
