list = ('Pencil', 1.75, 'Eraser', 2, 'Notebook', 5.50,
        'Pencil Case', 3.50, 'Scissors', 2.80, 'Ruler', 1.25,
        'Backpack', 10.50, 'Pens', 4.60, 'Books', 25)
print('-' * 40)
print(f'{"PRICE LIST":^40}')
print('-' * 40)
for item in range(0, len(list)):
    if item % 2 == 0:
        print(f'{list[item]:.<30}', end='')
    else:
        print(f'€ {list[item]:>7.2f}')
print('-' * 40)
