frase = input()
dicionario_frase = {}

for letra in frase:
    if letra not in dicionario_frase:
        dicionario_frase[letra] = 1
    else:
        dicionario_frase[letra] = dicionario_frase[letra] + 1

lista_digitos = []
for letra in frase:
    if letra not in lista_digitos:
        lista_digitos.append(letra)

lista_digitos.sort()
lista_digitos.reverse()
for letra in lista_digitos:
    print(letra, dicionario_frase[letra])

