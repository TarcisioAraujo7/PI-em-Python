contador = int(input())
loja = {}

for _ in range(contador):
    codigo = int(input())
    descricao = input()
    preco = float(input())
    loja[codigo] = preco

soma = 0
while True:
    cod = int(input())
    if cod == 0:
        break
    quant = int(input())
    if quant <= 0:
        continue
    if cod in loja:
        soma = soma + (loja[cod] * quant)

print('%3.2f' % soma)
