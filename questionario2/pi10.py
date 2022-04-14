altura = float(input())
raio = float(input())
pi = 3.14

volume = pi * raio ** 2 * altura
area = 2 * pi * raio ** 2 + 2 * pi * raio * altura

print('%3.2f' % volume)
print('%3.2f' % area)
