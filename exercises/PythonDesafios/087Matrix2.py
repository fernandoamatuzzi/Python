matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sumeven = higher = sumcol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input(f'Enter a number for [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^5}]', end='')
        if matrix[l][c] % 2 == 0:
            sumeven += matrix[l][c]
    print()
print('-=' * 30)
print(f'The sum of even numbers is {sumeven}.')
for l in range(0, 3):
    sumcol += matrix[l][2]
print(f'The sum of the numbers on the third column is {sumcol}.')
for c in range(0, 3):
    if c == 0:
        higher = matrix[1][c]
    elif matrix[1][c] > higher:
        higher = matrix[1][c]
print(f'The higher number on the second line is {higher}')
