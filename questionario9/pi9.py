valor = int(input())


def exibe_linhas(num):
    for numero in range(0, num + 1):
        print(((str(numero) + '-') * numero).rstrip('-'))


exibe_linhas(valor)
