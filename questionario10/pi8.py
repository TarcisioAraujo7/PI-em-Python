pesquisas = int(input())
candidato = input().split()
concorrente = input().split()


def vantagem(candidato, concorrente, n):
    contador = 0
    maior = -1
    while contador < n:
        diferenca = float(candidato[contador]) - float(concorrente[contador])
        if diferenca > 0 and diferenca > maior:
            maior = diferenca
        contador = contador + 1
    if maior == -1 or maior <= 0:
        return 0.00
    else:
        return maior


print('%3.2f' % vantagem(candidato, concorrente, pesquisas))
