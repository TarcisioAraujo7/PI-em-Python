provas_realizadas = int(input())
cpfs = []
notas = []
for _ in range(provas_realizadas):
    cpf = input()
    cpfs.append(cpf)

for _ in range(provas_realizadas):
    nota = input()
    notas.append(nota)

testes = int(input())

for _ in range(testes):
    teste = input()
    if teste in cpfs:
        print(notas[cpfs.index(teste)])
    else:
        print('NAO SE APRESENTOU')
