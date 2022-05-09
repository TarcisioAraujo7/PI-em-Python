partida1 = int(input())
partida2 = int(input())
partida3 = int(input())
partida4 = int(input())
partida5 = int(input())
partida6 = int(input())

soma = partida1 + partida2 + partida3 + partida4 + partida5 + partida6

if soma >= 100:
    print('Classificado')

if soma < 100:
    print('Eliminado')