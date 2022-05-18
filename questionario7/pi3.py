valor1 = int(input())
valor2 = int(input())
valor3 = int(input())

if valor1 <= valor2 <= valor3 or valor3 <= valor2 <= valor1:
    print(valor2)
elif valor2 <= valor1 <= valor3 or valor3 <= valor1 <= valor2:
    print(valor1)
elif valor1 <= valor3 <= valor2 or valor2 <= valor3 <= valor1:
    print(valor3)
