palavra = input()
remover = input()

for letra in remover:
    if letra in palavra:
        palavra = palavra.replace(letra, '')

print(palavra)
