salario = float(input())
imposto = 0

if salario <= 2000:
    print('Isento')
else:
    if 2000 < salario <= 3000:
        imposto = imposto + ((salario-2000)/100*8)
    elif 3000 < salario <= 4500:
        imposto = imposto + ((salario-3000)/100*18) + (1000/100*8)
    elif salario > 4500:
        imposto = imposto + ((salario - 4500)/ 100 * 28) + (1500 / 100 * 18) + (1000 / 100 * 8)
    print('R$', '%3.2f' % imposto)
