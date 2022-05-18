
def tipo_triangulo(l1, l2, l3):
    if l1 < (l2 + l3) and l2 < (l1 + l3) and l3 < (l1 + l2):
        if l1 == l2 and l2 == l3:
            return 'EQUILATERO'
        elif (l1 == l2 and l1 != l3) or (l1 == l3 and l1 != l2) or (l2 == l3 and l2 != l1):
            return 'ISOSCELES'
        elif l1 != l2 or l1 != l3 or l2 != l3:
            return "ESCALENO"
    else:
        return 'INVALIDO'


while True:
    entrada = input()
    if entrada == 'FIM':
        break
    valores = entrada.split()
    lado1 = int(valores[0])
    lado2 = int(valores[1])
    lado3 = int(valores[2])
    print(tipo_triangulo(lado1, lado2, lado3))
