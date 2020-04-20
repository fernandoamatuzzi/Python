import math
opp = float(input('Size of the opposite side: '))
adj = float(input('Size of the adjacent side: '))
'''hy = (opp ** 2 + adj ** 2) ** (1/2)
print('The hypotenuse is {:.2f}.'.format(hy))'''
hy = math.hypot(opp, adj)
print('The hypotenuse is {:.2f}.'.format(hy))
