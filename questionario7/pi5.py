galao_dolar = float(input())
litro_real = float(input())
cotacao_dolar = float(input())

litroEUA_real = (galao_dolar / 3.8) * cotacao_dolar

print('Gasolina EUA: R$', '%3.2f' % litroEUA_real)
print('Gasolina Brasil: R$', '%3.2f' % litro_real)
if litro_real > litroEUA_real:
    print('Mais barata nos EUA')
elif litroEUA_real > litro_real:
    print('Mais barata no Brasil')
else:
    print('Igual')
