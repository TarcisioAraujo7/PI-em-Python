contador = int(input())
amigo_secreto = {}

for _ in range(contador):
    entrada = input().split()
    amigo_secreto[entrada[0]] = entrada[1:]

while True:
    entrada = input().split()
    if entrada[0] == 'FIM':
        break
    if entrada[1] in amigo_secreto[entrada[0]]:
        print('Uhul! Seu amigo secreto vai adorar')
    else:
        print('Tente Novamente!')
