def superDigito(num):
    novonum = 0
    if len(num) == 1:
        return num
    else:
        for x in num:
            novonum = int(x) + novonum
        return superDigito(str(novonum))


entrada = input().split()
n = entrada[0]
k = int(entrada[1])
print(superDigito(n * k))
