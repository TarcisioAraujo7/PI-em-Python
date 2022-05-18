leituras = int(input())

while leituras > 0:
    contador = 0
    palavra = input()
    for letra in palavra:
        if letra == 'B':
            contador = contador + 2
        elif letra == 'Q' or letra == 'R' or letra == 'O' or letra == 'P' or letra == 'A' or letra == 'D':
            contador = contador + 1
    print(contador)
    leituras = leituras - 1
