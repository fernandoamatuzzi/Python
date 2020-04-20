import math
ang = float(input('Enter the angle: '))
sine = math.sin(math.radians(ang))
cosine = math.cos(math.radians(ang))
tangent = math.tan(math.radians(ang))
print('The angle is {}°. \nThe sine is {:.2f}. \nThe cosine is {:.2f}. \nThe tangent is {:.2f}.'.format(ang, sine, cosine, tangent))
