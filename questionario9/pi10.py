numX = int(input())
numY = int(input())


def ePrimo(valor):
    contador = 2
    while contador < valor:
        if valor % contador == 0:
            return False
        contador = contador + 1
    return True


if not (ePrimo(numX)):
    print('O numero', numX, 'nao eh primo')
elif not (ePrimo(numY)):
    print('O numero', numY, 'nao eh primo')
elif not (ePrimo(numX + numY)):
    print('A soma de', numX, 'e', numY, 'nao eh primo')
else:
    print('A soma de', numX, 'e', numY, 'eh um primo')

