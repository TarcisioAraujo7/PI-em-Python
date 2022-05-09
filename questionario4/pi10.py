consumo = int(input())
valor = 1.35

if 100 <= consumo <= 299:
    valor = 1.55
elif 300 <= consumo <= 574:
    valor = 1.75
elif 575 <= consumo:
    valor = 2.15

total = consumo * valor

if consumo > 300:
    total = total + ((total/100) * 10)

if total < 35:
    total = 35

print('%3.2f' % total)
print(valor)
