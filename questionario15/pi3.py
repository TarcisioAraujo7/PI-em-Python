
def quantos_dias(comida):
    if comida <= 1:
        return 0
    else:
        comida = comida / 2
        return 1 + quantos_dias(comida)


rep = int(input())
for _ in range(rep):
    numero = float(input())
    print(quantos_dias(numero), 'dias')
