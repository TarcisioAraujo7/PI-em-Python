entrada = input()
valores = entrada.split()
comeco = int(valores[0])
fim = int(valores[1])
contador = comeco
total = ''

while contador <= fim:
    if contador == fim:
        if contador % 5 == 0:
            total = total + str(contador)
    else:
        if contador % 5 == 0:
            total = total + str(contador) + '|'
    contador = contador + 1
if len(total) == 2:
    total = total[0]
print(total)
