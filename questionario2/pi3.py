entrada = input()
valores = entrada.split()
consumo = float(valores[0])
custo = float(valores[1])

valor_agua = consumo * 1000 * custo
valor_esgoto = valor_agua/100 * 80
total = valor_esgoto + valor_agua

print('%3.2f' % valor_agua)
print('%3.2f' % valor_esgoto)
print('%3.2f' % total)
