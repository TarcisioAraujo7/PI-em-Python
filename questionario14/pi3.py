passageirosidade = {}
passageirospoltrona = {}
idades = []

while True:
    numero_passagem = int(input())
    if numero_passagem == -1:
        break
    data = input()
    de = input()
    para = input()
    horario = input()
    poltrona = int(input())
    idade = int(input())
    nome = input()
    idades.append(idade)
    passageirosidade[nome] =  idade
    passageirospoltrona[nome] =  poltrona


media = sum(idades) / len(idades)

for passageiro in passageirosidade:
    if passageirosidade[passageiro] > media and passageirospoltrona[passageiro] % 2 == 0:
        print(passageiro)
