posicao = input()
limiar = int(input())
ordem_matriz = int(input())
matriz = []

for _ in range(ordem_matriz):
    linha = input().split()
    linha_num = [int(x) for x in linha]
    matriz.append(linha_num)

soma = 0
for x in range(len(matriz)):
    for y in range(len(matriz[x])):
        if posicao == 'acima' and y > x:
            soma = soma + matriz[x][y]
        elif posicao == 'abaixo' and y < x:
            soma = soma + matriz[x][y]

print(soma > limiar)
