leituras = int(input())


def eh_invalida(riso):
    if len(riso) > 50:
        return True
    vogais = 0
    for letra in riso:
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            vogais = vogais + 1
    if vogais == 0:
        return True
    else:
        return False


def eh_engracada(riso):
    vogais = ''
    vogaiscontrario = ''
    for letra in riso:
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            vogais = vogais + letra
    for vogal in vogais:
        vogaiscontrario = vogal + vogaiscontrario
    if vogais == vogaiscontrario:
        return True
    else:
        return False


while leituras > 0:
    risada = input()
    if eh_invalida(risada):
        print('INVALIDA')
    else:
        if eh_engracada(risada):
            print('ENGRACADA')
        else:
            print('SEM GRACA')

    eh_engracada(risada)
    leituras = leituras - 1
