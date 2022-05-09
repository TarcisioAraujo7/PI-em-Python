media = float(input())
faltas = int(input())


def classifica_aluno(mediaf, faltasf):
    if faltasf > 10:
        return 'REPROVADO POR FALTAS'
    elif mediaf >= 9.5:
        return 'APROVADO COM LOUVOR'
    elif mediaf >= 7:
        return 'APROVADO'
    else:
        return 'REPROVADO'


print(classifica_aluno(media, faltas))
