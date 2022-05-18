contador = 101
lista = []
numero_final = 0

while contador != 0:
    numero = int(input())
    if contador == 1:
        numero_final = numero
    lista.append(numero)
    contador = contador - 1

contador2 = 0
for num in lista:
    if num == numero_final and contador2 != 100:
        print(contador2)
    contador2 = contador2 + 1
