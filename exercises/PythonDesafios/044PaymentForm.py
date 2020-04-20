print('=' * 40)
print('{:=^40}'.format(' THE GOOD PRICE STORE '))
print('=' * 40)
price = float(input('Price of the products: '))
option = int(input('''PAYMENT FORM:
[ 1 ] Cash (10% discount)
[ 2 ] Debit Card (5% discount)
[ 3 ] 2 X Credit Card (normal price)
[ 4 ] 3 X or more Credit Card (+ 20% interest)
Your option: '''))
if option == 1:
    final = price - (price * 10 / 100)
    print('Your purchase is \33[1;30m€{:.2f}\33[m and the final price is \33[1;34m€{:.2f}\33[m.'.format(price, final))
elif option == 2:
    final = price - (price * 5 / 100)
    print('Your purchase is \33[1;30m€{:.2f}\33[m and the final price is \33[1;34m€{:.2f}\33[m.'.format(price, final))
elif option == 3:
    inst = price / 2
    print('The final price remains the same, \33[1;30m€{:.2f}\33[m in \33[1;31m2\33[m installments of \33[1;33m€{'
          ':.2f}\33[m.'.format(price, inst))
elif option == 4:
    months = int(input('How many installments: '))
    final = price + (price * 20 / 100)
    inst = final / months
    print('Your purchase is \33[1;30m€{:.2f}\33[m and the final price will be \33[1;34m€{:.2f}\33[m in \33[1;31m{'
          ':.0f}\33[m installments of \33[1;33m€{:.2f}\33[m.'.format(price, final, months, inst))
else:
    print('\33[1;4;31mInvalid option. Please try again!')
