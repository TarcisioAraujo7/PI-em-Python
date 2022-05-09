n = int(input())
m = int(input())
contador = n

while contador <= m:
    if contador % 2 != 0:
        print(contador)
        contador = contador + 1
    else:
        contador = contador + 1
