entrada = input()
valores = entrada.split()
valorx = int(valores[0])
valory = int(valores[1])
contador = 1
lista = ''

for num in range(1, valory + 1):
    if num < valorx * contador:
        lista = lista + str(num) + ' '
    else:
        lista = lista + str(num)
        contador = contador + 1
        print(lista)
        lista = ''

print(lista)