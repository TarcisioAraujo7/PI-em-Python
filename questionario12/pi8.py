def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)


soma = 0
for _ in range(5):
    inteiro = int(input())
    if inteiro % 3 == 0:
        soma = fatorial(inteiro) + soma

print(soma)
