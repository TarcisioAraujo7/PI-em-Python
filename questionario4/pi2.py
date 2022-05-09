valor = float(input())
anos_garantia = int(input())

if anos_garantia == 2:
    valor = valor + ((valor/100) * 5)
elif anos_garantia == 1:
    valor = valor + ((valor / 100) * 3)

print('%3.2f' % valor)
