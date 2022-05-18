entrada = int(input())
contador = 1

while entrada >= contador:
    print(contador, contador * contador, contador * contador * contador)
    print(contador, (contador * contador) + 1, (contador * contador * contador) + 1)
    contador = contador + 1
