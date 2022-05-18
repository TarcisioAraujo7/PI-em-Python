palavra = input()
letra = input()
contador = 0

for caracter in palavra:
    if caracter == letra:
        contador = contador + 1

print(contador)
