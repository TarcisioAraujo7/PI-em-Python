vel_init1 = float(input())
aceleracao1 = float(input())
tempo1 = float(input())
vel_init2 = float(input())
aceleracao2 = float(input())
tempo2 = float(input())
vel_init3 = float(input())
aceleracao3 = float(input())
tempo3 = float(input())


def velkmh(vel, ac, tempo):
    velkm = 3.6 * (vel + ac * tempo)
    return velkm


def compara2(valor1, valor2):
    if valor1 <= valor2:
        return valor1
    else:
        return valor2


print('%2.1f' % compara2((compara2(velkmh(vel_init1, aceleracao1, tempo1), velkmh(vel_init2, aceleracao2, tempo2))), velkmh(vel_init3, aceleracao3, tempo3)))
