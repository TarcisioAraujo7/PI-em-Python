dia = int(input())
mes = int(input())


def estacao_ano(dd, mm):
    if 9 <= mm <= 11:
        if mm == 10 or mm == 11:
            return 'PRIMAVERA'
        elif mm == 9 and dd >= 21:
            return 'PRIMAVERA'
    elif mm <= 3:
        if mm == 1 or mm == 2:
            return 'VERAO'
        elif mm == 3 and dd <= 20:
            return 'VERAO'
    elif mm == 12:
        if dd >= 21:
            return 'VERAO'
        else:
            return 'PRIMAVERA'
    elif 3 <= mm <= 6:
        if mm == 4 or mm == 5:
            return 'OUTONO'
        elif mm == 3 and dd >= 21:
            return 'OUTONO'
        elif mm == 6 and dd <= 20:
            return 'OUTONO'
    else:
        return 'INVERNO'


print(estacao_ano(dia, mes))
