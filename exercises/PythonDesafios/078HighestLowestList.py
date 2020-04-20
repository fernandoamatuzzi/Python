values = []
higher = lower = 0
for c in range(0, 5):
    values.append(int(input(f'Enter a number for the position {c}: ')))
    if c == 0:
        higher = lower = values[c]
    else:
        if values[c] > higher:
            higher = values[c]
        if values[c] < lower:
            lower = values[c]
print('=-' * 30)
print(f'You entered: {values}')
print(f'The higher value entered was {higher} in the position(s) ', end='')
for i, v in enumerate(values):
    if v == higher:
        print(f'{i}... ', end='')
print()
print(f'The lower value entered was {lower} in the position(s) ', end='')
for i, v in enumerate(values):
    if v == lower:
        print(f'{i}... ', end='')
print()
