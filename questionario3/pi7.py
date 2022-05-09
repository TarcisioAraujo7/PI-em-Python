diametro_bola = int(input())
entrada = input()
valores = entrada.split()
altura = int(valores[0])
largura = int(valores[1])
profundidade = int(valores[2])

if diametro_bola <= altura and diametro_bola <= largura and diametro_bola <= profundidade:
    print('S')

if diametro_bola > altura or diametro_bola > largura or diametro_bola > profundidade:
    print('N')
