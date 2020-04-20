num = []
for c in range(0, 5):
    n = int(input('Enter a number: '))
    if c == 0 or n > num[-1]:
        num.append(n)
        print('Added at the end of the list.')
    else:
        pos = 0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos, n)
                print(f'Added an the position {pos} in the list.')
                break
            pos += 1
print('-=' * 30)
print(f'The values entered in order were {num}.')
