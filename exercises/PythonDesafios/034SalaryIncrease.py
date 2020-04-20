sal = float(input('What is the salary of the employee? '))
print('The current salary is €{:.2f}.'.format(sal))
if sal > 1250:
    r = 10
    nsal = sal * (10/100) + sal
else:
    r = 15
    nsal = sal * (15/100) + sal
print('The new salary, after the raise of {}%, is €{:.2f}.'.format(r, nsal))
