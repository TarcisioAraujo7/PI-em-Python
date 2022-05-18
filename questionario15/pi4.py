def eh_primo(num):
    saida = False
    if -1 <= num <= 1:
        saida = False
    elif num > 3:
        for x in range(2, num):
            if num % x == 0:
                saida = False
                break
            else:
                saida = True
    else:
        saida = True
    return saida


lista = input().split()
listaint = [int(x) for x in lista]
primos = [x for x in listaint if eh_primo(x)]
if len(primos) == 4:
    print(primos[0] * primos[1] * primos[2] * primos[3])
else:
    print('SEM PRODUTO')
