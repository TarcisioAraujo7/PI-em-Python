leituras = int(input())
contador1 = 0
contador2 = 0
lista1 = []
lista2 = []
resultado = []

while contador1 < leituras:
    entrada = input()
    lista1.append(entrada)
    contador1 = contador1 + 1

while contador2 < leituras:
    entrada = input()
    lista2.append(entrada)
    contador2 = contador2 + 1

while len(resultado) != 2 * leituras:
    for elemento in range(leituras):
        resultado.append(lista1[elemento])
        resultado.append(lista2[elemento])

for digito in resultado:
    print(digito)
