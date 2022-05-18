entrada = input().split()
linhasA = int(entrada[0])
linhasB = int(entrada[1])
colunasB = int(entrada[2])
matrizA = []
matrizB = []
matrizC = [[0] * colunasB for _ in range(linhasA)]

for _ in range(linhasA):
    linha = input().split()
    linha_num = [int(x) for x in linha]
    matrizA.append(linha_num)

for _ in range(linhasB):
    linha = input().split()
    linha_num = [int(x) for x in linha]
    matrizB.append(linha_num)


def mult_soma(linha, coluna):
    soma = 0
    for x in range(len(linha)):
        soma = soma + (linha[x] * coluna[x])
    return soma


def pega_coluna(matriz, coluna):
    resultado = []
    for x in matriz:
        resultado.append(x[coluna])
    return resultado


for x in range(len(matrizC)):
    for y in range(len(matrizC[x])):
        matrizC[x][y] = (mult_soma(matrizA[x], pega_coluna(matrizB, y)))


for linha in matrizC:
    saida = ''
    for elemento in linha:
        if elemento == linha[-1]:
            saida = saida + str(elemento)
        else:
            saida = saida + str(elemento) + ' '
    print(saida)
