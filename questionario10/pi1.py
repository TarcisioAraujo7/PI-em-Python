lista_inicial = list()

while True:
    nome = input()
    if nome == "FIM":
        break
    lista_inicial.append(nome)

contador = 0

while True:
    contagens = int(input())
    lista_inicial.sort()
    for nome in lista_inicial:
        print(nome)
    if contagens == 0:
        break
    print("-" * 50)
    while contador < contagens:
        nome = input()
        lista_inicial.append(nome)
        contador = contador + 1
    contador = 0
