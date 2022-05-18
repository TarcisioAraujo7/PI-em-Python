def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)


while True:
    num = int(input())
    if num == -1:
        break
    print(fatorial(num))
