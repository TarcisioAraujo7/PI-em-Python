m = int(input())
n = int(input())
mult = 0
multiplo = 0

while mult <= n:
    multiplo = mult * m
    mult = mult + 1

if m > n:
    print('Sem multiplos menores que', n)
else:
    print(multiplo - m)
