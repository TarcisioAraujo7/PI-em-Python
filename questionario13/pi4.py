gabarito = input()
lista_gab = []
[lista_gab.append(x) for x in gabarito]
notamaior = {}


def corrige(respostas, gabarito):
    lista_resp = []
    [lista_resp.append(x) for x in respostas[0]]
    saida = 0
    for i in range(len(gabarito)):
        if lista_resp[i] == gabarito[i]:
            saida = saida + 1
    return float(saida)


notas = []
alunoslist = []
while True:
    entrada = input().split()
    num_aluno = entrada[0]
    questoes = entrada[1:]
    if int(entrada[0]) == 9999:
        break
    alunoslist.append(int(num_aluno))
    notas.append(corrige(questoes, lista_gab))
    print(num_aluno, corrige(questoes, lista_gab))

for x in notas:
    if x not in notamaior:
        notamaior[x] = 1
    else:
        notamaior[x] = notamaior[x] + 1

notas = [x for x in notas if x >= 6]

porcentagem = len(notas) * 100 / alunoslist[-1]
print('%3.1f' % porcentagem + '%')

moda = -1
for x in notamaior:
    if x >= moda:
        moda = x

print(notamaior)
