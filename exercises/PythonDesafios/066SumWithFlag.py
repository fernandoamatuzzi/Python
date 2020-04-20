sum = count = 0
while True:
    num = int(input('Enter a number (999 to stop): '))
    if num == 999:
        break
    count += 1
    sum += num
print(f'The sum of {count} numbers is {sum}.')
