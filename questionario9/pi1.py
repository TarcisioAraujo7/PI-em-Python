leituras = int(input())

while leituras > 0:
    vogais = input()
    frase = input()
    contador = 0
    for letra in frase:
        if letra in vogais:
            contador = contador + 1
    leituras = leituras - 1
    print(contador)
