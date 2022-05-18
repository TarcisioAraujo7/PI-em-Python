votosSIM = 0
votosNAO = 0
votosNULO = 0

while True:
    voto = input()
    votoFormatado = voto.lower()
    if votoFormatado == 'sim':
        votosSIM = votosSIM + 1
        continue
    elif votoFormatado == 'nao':
        votosNAO = votosNAO + 1
        continue
    elif votoFormatado == 'nulo':
        votosNULO = votosNULO + 1
        continue
    elif votoFormatado == 'encerrar':
        break

if votosSIM > (votosNAO+votosNULO):
    print('COM FOGOS')
else:
    print('SEM FOGOS')
