def formata(texto, cont):
    contador = cont
    palavra_formatada = ' '
    print(texto[contador])
    if contador == len(texto):
        return ''
    else:
        if texto[contador] == palavra_formatada[-1]:
            return palavra_formatada + formata(texto, cont + 1)
        else:
            return palavra_formatada + texto[contador] + formata(texto, cont + 1)


while True:
    frase = input()
    if frase == '*':
        break
    print(formata(frase, 0))

# DESISTI DESSA
