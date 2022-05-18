numero = int(input())


def pares(num):
    if num == 0:
        return print(0)
    else:
        if num % 2 == 0:
            return print(num), pares(num-2)
        else:
            return pares(num-1)


pares(numero)
