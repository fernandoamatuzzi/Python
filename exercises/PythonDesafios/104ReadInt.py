def readInt(msg):
    ok = False
    value = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            value = int(n)
            ok = True
        else:
            print('\033[0;31mERROR! Enter a valid integer number.\033[m')
        if ok:
            break
    return value


'''def leiaInt(num):
    while True:
        valor = str(input(num))
        if valor.isnumeric():
            valor = int(valor)
            return valor
            break
        else:
            print('\033[31mErro! Digite um número inteiro válido!\033[m')'''


n = readInt('Enter a number: ')
print(f'You entered the number {n}.')
