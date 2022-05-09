hemisferio = int(input())
dia = int(input())
mes = int(input())


def estacao_ano(dd, mm, hemis):
    if hemis == 1:
        if mm == 1 or mm == 2:
            return 'VERAO'
        elif mm == 3:
            if dd < 21:
                return 'VERAO'
            else:
                return 'OUTONO'
        elif mm == 4 or mm == 5:
            return 'OUTONO'
        elif mm == 6:
            if dd < 21:
                return 'OUTONO'
            else:
                return 'INVERNO'
        elif mm == 7 or mm == 8:
            return 'INVERNO'
        elif mm == 9:
            if dd < 21:
                return 'INVERNO'
            else:
                return 'PRIMAVERA'
        elif mm == 10 or mm == 11:
            return 'PRIMAVERA'
        elif mm == 12:
            if dd < 21:
                return 'PRIMAVERA'
            else:
                return 'VERAO'
    elif hemis == 0:
        if mm == 1 or mm == 2:
            return 'INVERNO'
        elif mm == 3:
            if dd < 21:
                return 'INVERNO'
            else:
                return 'PRIMAVERA'
        elif mm == 4 or mm == 5:
            return 'PRIMAVERA'
        elif mm == 6:
            if dd < 21:
                return 'PRIMAVERA'
            else:
                return 'VERAO'
        elif mm == 7 or mm == 8:
            return 'VERAO'
        elif mm == 9:
            if dd < 21:
                return 'VERAO'
            else:
                return 'OUTONO'
        elif mm == 10 or mm == 11:
            return 'OUTONO'
        elif mm == 12:
            if dd < 21:
                return 'OUTONO'
            else:
                return 'INVERNO'


print(estacao_ano(dia, mes, hemisferio))
