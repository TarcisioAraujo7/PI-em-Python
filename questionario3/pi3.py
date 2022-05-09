dias = int(input())
quilometragem = int(input())
quilometragem_max = 100 * dias
valor_total = dias * 90

if quilometragem > quilometragem_max:
    valor_total = valor_total + ((quilometragem - quilometragem_max) * 12)

print('%3.2f' % valor_total)
