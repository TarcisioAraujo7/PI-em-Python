entradas = int(input())
contador = 0
notas = []

while contador < entradas:
    entrada = float(input())
    notas.append(entrada)
    contador = contador + 1

media = sum(notas) / entradas

acima10 = [x for x in notas if x - media > media * 0.1]
abaixo10 = [x for x in notas if x - media < media * 0.1]

print('%3.2f' % media)
print(len(acima10))
print(len(abaixo10))
