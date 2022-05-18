turma_tam = {}
turma_cor = {}

while True:
    entrada = int(input())
    if entrada == 0:
        break
    for _ in range(entrada):
        nome = input()
        dados = input().split()
        turma_tam[nome] = dados[1]
        turma_cor[nome] = dados[0]
    for aluno in turma_cor:
        if turma_cor[aluno] == 'branco' and turma_tam[aluno] == 'P':
            print(aluno)

