mult1 = int(input())
mult2 = int(input())
contador = 0


def mult_somas(num1, num2):
    if num2 <= 0:
        return 0
    else:
        return num1 + mult_somas(num1, num2 - 1)


print(mult_somas(abs(mult1), abs(mult2)))
