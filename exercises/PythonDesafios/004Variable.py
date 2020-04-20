n = input('Type something: ')
print('Is {} a number? '.format(n), n.isnumeric())
print('Is {} alphanumeric? '.format(n), n.isalnum())
print('Is {} a letter? '.format(n), n.isalpha())
print('Is {} a decimal number? '.format(n), n.isdecimal())
print('Is {} all lowercase? '.format(n), n.islower())
print('Is {} all uppercase? '.format(n), n.isupper())
print('Is {} printable? '.format(n), n.isprintable())

