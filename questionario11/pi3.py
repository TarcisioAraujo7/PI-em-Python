entrada = input().split()
linhas = int(entrada[0])
coluna = int(entrada[1])
matriz = []

for _ in range(linhas):
    linha = input().split()
    linha_num = [int(x) for x in linha]
    matriz.append(linha_num)
