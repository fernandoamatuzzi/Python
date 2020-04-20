height = float(input('Enter the height of the wall in meters: '))
width = float(input('Enter the width of the wall in meters: '))
area = height * width
paint = area / 2
print("Your wall's dimension is {}m x {}m, so the area is {}m².".format(height, width, area))
print("To paint this wall, you will need {}l of paint".format(paint))
