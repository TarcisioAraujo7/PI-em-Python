lista = input().split()
maior = 0

for numero in lista:
    if maior < int(numero):
        maior = int(numero)

print(maior)
