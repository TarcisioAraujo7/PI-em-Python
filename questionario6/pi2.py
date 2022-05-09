num1 = int(input())
num2 = int(input())
soma = 0

if num1 <= num2:
    while num1 <= num2:
        if num1 >= 0:
            soma = soma + num1
            num1 = num1 + 1
        else:
            num1 = num1 + 1
else:
    while num2 <= num1:
        if num2 >= 0:
            soma = soma + num2
            num2 = num2 + 1
        else:
            num2 = num2 + 1
print(soma)
