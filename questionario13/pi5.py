aeroporto = {}

for _ in range(37):
    entrada = input().split()
    voo = entrada[0]
    lugares = int(entrada[1])
    aeroporto[voo] = lugares

while True:
    entrada = input().split()
    ident = int(entrada[0])
    if ident == 9999:
        break
    solicitacao = entrada[1]
    if solicitacao not in aeroporto:
        print('INDISPONIVEL')
        continue
    if aeroporto[solicitacao] > 0:
        aeroporto[solicitacao] = aeroporto[solicitacao] - 1
        print(ident)
    else:
        print('INDISPONIVEL')
