num1 = int(input())
num2 = int(input())
contador = 1
resultado = 0

if num1 and num2 != 0:
    while contador < 50:
        if contador % num1 == 0 and contador % num2 == 0:
            resultado = resultado + 1
        contador = contador + 1
    print(resultado)
else:
    print(0)

