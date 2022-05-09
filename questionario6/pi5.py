entradaLC = input()
valoresLC = entradaLC.split()
leituras = int(valoresLC[0])
capacidade = int(valoresLC[1])
contador = 0
limite = 'N'
no_elevador = 0

while contador != leituras:
    entradaES = input()
    valoresES = entradaES.split()
    saidas = int(valoresES[0])
    entradas = int(valoresES[1])
    if no_elevador > capacidade:
        limite = 'S'
    no_elevador = no_elevador + (entradas - saidas)
    contador = contador + 1

print(limite)
