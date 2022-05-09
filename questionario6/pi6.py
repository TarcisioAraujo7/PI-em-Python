quantidade = int(input())
contador = 1
total = 0
saida = ''
if quantidade > 0:
    while contador <= quantidade:
        total = total + (contador/(contador*3))
        if contador == quantidade:
            saida = saida + str(contador) + '/' + str(contador * 3)
        else:
            saida = saida + str(contador) + '/' + str(contador * 3) + ' + '
        contador = contador + 1

print(saida)
print('%3.2f' % total)
