def factorial(n=1, show=False):
    """
    -> Calculate the Factorial of a number.
    :param n: The number to be calculated.
    :param show: (optional) To show or not the calculation process.
    :return: The result of a Factorial of a number n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# print(factorial(5, False))
help(factorial)
