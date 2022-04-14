entrada = input()
valores = entrada.split()
valorA = float(valores[0])
valorB = float(valores[1])
valorC = float(valores[2])
pi = 3.14159

# calculo das áreas
triangulo = valorA * valorC / 2
circulo = valorC ** 2 * pi
trapezio = ((valorA + valorB) * valorC) / 2
quadrado = valorB ** 2
retangulo = valorA * valorB

print('TRIANGULO:', '%4.3f' % triangulo)
print('CIRCULO:', '%4.3f' % circulo)
print('TRAPEZIO:', '%4.3f' % trapezio)
print('QUADRADO:', '%4.3f' % quadrado)
print('RETANGULO:', '%4.3f' % retangulo)
