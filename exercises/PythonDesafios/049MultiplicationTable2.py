n = int(input('Enter a number to check the multiplication table: '))
print('-' * 12)
for c in range(0, 11):
    print('{} x {:2} = {}'.format(n, c, n*c))
print('-' * 12)
