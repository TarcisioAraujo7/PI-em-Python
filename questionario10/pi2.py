comprimento = int(input())
lista = input().split()
lista.sort()
resultado = []
string = ''
pos = -1

for numero in lista:
    if pos != lista.index(numero):
        resultado.append(numero)
        pos = lista.index(numero)

for num in resultado:
    string = string + num

print(' '.join(string))
