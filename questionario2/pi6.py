valor = int(input())
notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
notas2 = 0
notas1 = 0

print(valor)
if valor > 0 and valor < 1000000:
    notas100 = notas100 + valor / 100
    valor = valor - int(notas100) * 100

    notas50 = notas50 + valor / 50
    valor = valor - int(notas50) * 50

    notas20 = notas20 + valor / 20
    valor = valor - int(notas20) * 20

    notas10 = notas10 + valor / 10
    valor = valor - int(notas10) * 10

    notas5 = notas5 + valor / 5
    valor = valor - int(notas5) * 5

    notas2 = notas2 + valor / 2
    valor = valor - int(notas2) * 2

    notas1 = notas1 + valor / 1
    valor = valor - int(notas1) * 1

print(int(notas100), 'nota(s) de R$ 100,00')
print(int(notas50), 'nota(s) de R$ 50,00')
print(int(notas20), 'nota(s) de R$ 20,00')
print(int(notas10), 'nota(s) de R$ 10,00')
print(int(notas5), 'nota(s) de R$ 5,00')
print(int(notas2), 'nota(s) de R$ 2,00')
print(int(notas1), 'nota(s) de R$ 1,00')
