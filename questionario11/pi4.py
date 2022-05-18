matrizes = int(input())
correto = True


def pega_coluna(matriz, coluna):
    resultado = []
    for x in matriz:
        resultado.append(x[coluna])
    return resultado



for numero in range(matrizes):

    matriz = []
    for _ in range(9):
        linha = input().split()
        linha_num = [int(x) for x in linha]
        for x in linha_num:
            if x not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                correto = False
        matriz.append(linha_num)

    for x in matriz:
        if sum(x) != 45:
            correto = False

    for num in range(9):
        if sum(pega_coluna(matriz, num)) != 45:
            correto = False

    if correto:
        print('Instancia', numero + 1)
        print('SIM')
        print()
    else:
        print('Instancia', numero + 1)
        print('NAO')
        print()
