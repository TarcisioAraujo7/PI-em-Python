livros = int(input())
alunos = int(input())

media = float(alunos / livros)

print(media)

if media > 18:
    print('D')
elif 18 >= media >= 13:
    print('C')
elif 13 > media > 8:
    print('B')
else:
    print('A')
