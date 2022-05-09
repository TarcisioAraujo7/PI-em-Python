limite = int(input())
contagem = 0
total = 0

while contagem < limite:
    if contagem % 3 == 0 or contagem % 5 == 0:
        total = total + contagem
        contagem = contagem + 1
    else:
        contagem = contagem + 1

print(total)
