salario = float(input())
aumento = float(input())

att_salario = salario + (salario/100 * aumento)

print('Seu salario teve aumento de', aumento, '%, passando de R$', salario, 'para R$', att_salario)
