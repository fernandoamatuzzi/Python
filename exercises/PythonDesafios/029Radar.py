vel = float(input('What is the speed of your car? '))
if vel > 80:
    fee = (vel - 80) * 7
    print('You exceeded the speed limit of 80km/h! You need to pay a fee of €{:.2f}!'.format(fee))
print('Have a good day! Drive safe!')
