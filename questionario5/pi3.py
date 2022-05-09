entrada = input()
valores = entrada.split()
num1 = int(valores[0])
num2 = int(valores[1])
num3 = int(valores[2])


def maior2(val1, val2):
    return (val1+val2+(abs(val1-val2)))/2


def maior3(valor1, valor2, valor3):
    return maior2(maior2(valor1, valor2), valor3)


print(int(maior3(num1, num2, num3)), 'eh o maior')
