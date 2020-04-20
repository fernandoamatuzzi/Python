g1 = float(input('First grade: '))
g2 = float(input('Second grade: '))
a = float(g1 + g2)/2
print('Your first grade is {:.1f} and your second grade is {:.1f}.'.format(g1, g2))
if a < 5:
    print('Your average grade is {:.1f}. \33[1;31mREPROVED!'.format(a))
elif 5 <= a <= 6.9:
    print('Your average grade is {:.1f}. \33[1;33mRECOVERY!'.format(a))
elif a >= 7:
    print('Your average grade is {:.1f}. \33[1;34mAPPROVED! \33[1;36mCONGRATULATIONS!'.format(a))
