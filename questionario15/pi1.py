def fatorial(z):
    if z == 0:
        return 1
    else:
        return z * fatorial(z-1)


def eh_primo(num):
    saida = False
    if num == 0 :
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


def proximo_primo(y):
    if eh_primo(y):
        return y
    elif eh_primo(y+1):
        return y+1
    else:
        return proximo_primo(y+1)


saida = ''
total = 0
termos = int(input())
for numero in range(termos + 1):
    if numero != 0:
        total = total + ((fatorial(numero)) / proximo_primo(numero))
        if numero == termos:
            saida = saida + str(numero) + '!/' + str(proximo_primo(numero))
        else:
            saida = saida + str(numero) + '!/' + str(proximo_primo(numero)) + ' + '

print(saida)
print('%3.2f' % total)
