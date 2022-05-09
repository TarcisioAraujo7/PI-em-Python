entrada = input()
valores = entrada.split()
nota1 = float(valores[0])
nota2 = float(valores[1])
nota3 = float(valores[2])
nota4 = float(valores[3])


def analisar_situacao(n1, n2, n3, n4):
    media = (n1 * 1 + n2 * 2 + n3 * 3 + n4 * 4)/(1 + 2 + 3 + 4)
    if media >= 9:
        return 'aprovado com louvor'
    elif media >= 7:
        return 'aprovado'
    elif 3 <= media < 7:
        return 'prova final'
    else:
        return 'reprovado'


print(analisar_situacao(nota1, nota2, nota3, nota4))
