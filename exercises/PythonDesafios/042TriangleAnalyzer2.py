r1 = float(input('First straight: '))
r2 = float(input('Second straight: '))
r3 = float(input('Third straight: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('These 3 straights CAN form a ', end='')
    if r1 == r2 == r3:
        print('EQUILATERAL triangle!')
    elif r1 != r2 != r3 != r1:
        print('SCALENE triangle!')
    else:
        print('ISOSCELLES triangle!')
else:
    print('These 3 straights CANNOT form a triangle.')
