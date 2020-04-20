dis = float(input('What is the distance of your trip? '))
print('You are going to travel for {:.1f}km.'.format(dis))
'''if dis <= 200:
    price = dis * 0.50
else:
    price = dis * 0.45'''
price = dis * 0.50 if dis <= 200 else dis * 0.45
print('The price of your ticket will be €{:.2f}.'.format(price))
