consumo = float(input())
valor_pago = consumo * 1.50
valor_descontado = valor_pago - (valor_pago/100 * 15)

print('Valor a ser pago: R$', '%3.2f' % valor_pago, 'reais')
print('Valor a ser pago com desconto: R$', '%3.2f' % valor_descontado, 'reais')
