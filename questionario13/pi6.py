entrada = input().split()
regras = int(entrada[0])
linhas_txt = int(entrada[1])
correcao = {}

for _ in range(regras):
    entrada = input().split()
    correcao[entrada[0]] = correcao[entrada[0]] = entrada[-1]

for _ in range(linhas_txt):
    linha = input().split()
    for palavra in linha:
        if palavra in correcao:
            linha[linha.index(palavra)] = correcao[palavra]

    resultado = []

    linha = (' '.join(linha))
    for letra in linha:
        resultado.append(letra)

    for x in range(len(resultado)):
        if resultado[x] in correcao:
            resultado[x] = correcao[resultado[x]]

    print(resultado)
