listanumeros = input()
numeros = [int(x) for x in listanumeros]


def ContaDigitosPares(lista):
    if not lista:
        return 0
    else:
        if lista[0] % 2 == 0:
            return 1 + ContaDigitosPares(lista[1:])
        else:
            return ContaDigitosPares(lista[1:])


print(ContaDigitosPares(numeros))
