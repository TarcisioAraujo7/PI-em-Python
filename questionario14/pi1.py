registro = {}
while True:
    idade = int(input())
    if idade == -1:
        break
    dados = input().split()
    registro[idade] = dados

maior = 0
contador = 0
for cidadao in registro:
    if 'f' in registro[cidadao] and 'l' in registro[cidadao] and 'v' in registro[cidadao] and 18 <= cidadao <= 35:
        contador = contador + 1
    if cidadao >= maior:
        maior = cidadao

print('Mais velho:', maior)
print('Mulheres com olhos verdes, loiras com 18 a 35 anos:', '%3.2f' % (contador * 100 / len(registro)) + '%')
