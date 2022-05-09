lado1 = float(input())
lado2 = float(input())
lado3 = float(input())

if lado1 == lado3 and lado1 == lado2:
    print('equilatero')
elif lado1 == lado3 and lado1 != lado2 or lado2 == lado3 and lado1 != lado2 or lado1 == lado2 and lado3 != lado2:
    print('isosceles')
else:
    print('escaleno')

