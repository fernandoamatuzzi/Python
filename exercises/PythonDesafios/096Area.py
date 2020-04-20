def area(w, l):
    a = w * l
    print(f'The land area of {w}m width by {l}m length is {a}m2.')


print('Area Calculation')
print('-' * 20)
w = float(input('Width (m): '))
l = float(input('Length (m): '))
area(w, l)
