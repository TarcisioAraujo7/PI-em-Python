consumo = int(input())
total = 7

if 11 <= consumo <= 30:
    total = total + (consumo-10)
if 31 <= consumo <= 100:
    total = total + (consumo-30) * 2 + 20
if 101 <= consumo:
    total = total + (consumo-100) * 5 + 160

print(total)
