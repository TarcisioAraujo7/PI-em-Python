votos83 = 0
votos93 = 0
votos0 = 0
votosNULOS = 0

while True:
    voto = int(input())
    if voto == 83:
        votos83 = votos83 + 1
        continue
    elif voto == 93:
        votos93 = votos93 + 1
        continue
    elif voto == 0:
        votos0 = votos0 + 1
        continue
    if voto == -1:
        break
    else:
        votosNULOS = votosNULOS + 1
        continue

if votos93 > votos83:
    vencedor = 93
elif votos83 > votos93:
    vencedor = 83
else:
    vencedor = 93

totalvalidos = votos0 + votos83 + votos93
porcentagem83 = (votos83 * 100) / totalvalidos
porcentagem93 = (votos93 * 100) / totalvalidos


print(votos83)
print(votos93)
print(votos0)
print(votosNULOS)
print(vencedor)
print('%3.2f' % porcentagem83)
print('%3.2f' % porcentagem93)
