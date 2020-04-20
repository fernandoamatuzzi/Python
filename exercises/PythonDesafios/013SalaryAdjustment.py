sal = float(input('The current salary is € '))
i = 15
nsal = sal + (sal * i / 100)
print('An employee who receives € {:.2f} of salary, with a {}% increase will now receive € {:.2f}.'.format(sal, i, nsal))


