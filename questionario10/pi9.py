elementos = int(input())
lista = input().split()

listaint = [int(x) for x in lista]


print('Menor valor:', min(listaint))
print('Posicao:', listaint.index(min(listaint)))
