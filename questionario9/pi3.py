entrada = input()
valores = entrada.split()
investimento = float(valores[0])
taxa = float(valores[1])
anos = int(valores[2])
trimestres = anos * 4
contador = 0

while contador < trimestres:
    rendimento = investimento * taxa
    investimento = investimento + rendimento
    print('Rendimento:', '%3.2f' % rendimento, 'Montante:', '%3.2f' % investimento)
    contador = contador + 1
