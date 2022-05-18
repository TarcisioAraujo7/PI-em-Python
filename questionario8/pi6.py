leituras = int(input())

while leituras > 0:
    frase = input()
    fraseformatada = frase.lower()
    frase_sem_espaco = fraseformatada.replace(' ', '')
    frase_contrario = ''
    for letra in frase_sem_espaco:
        frase_contrario = letra + frase_contrario
    print(frase_sem_espaco)
    print(frase_contrario)
    if frase_sem_espaco == frase_contrario:
        print('SIM')
    else:
        print('NAO')
    leituras = leituras - 1
