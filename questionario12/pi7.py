def fibonacci(num):
    if num == 0 or num == 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


numero = int(input())

resultado = [fibonacci(x) for x in range(numero)]

string = ''
for y in resultado:
    if y == resultado[0]:
        string = str(y) + string
    else:
        string = str(y) + ' ' + string

print(string)
