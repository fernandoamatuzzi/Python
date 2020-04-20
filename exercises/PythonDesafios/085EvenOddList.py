num = [[], []]
values = 0
for c in range(1, 8):
    values = int(input(f'Enter number {c}: '))
    if values % 2 == 0:
        num[0].append(values)
    else:
        num[1].append(values)
print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'The even numbers are: {num[0]}')
print(f'The odd numbers are: {num[1]}')
