num1 = float(input())
num2 = float(input())
num3 = float(input())

media = (num1 + num2 + num3) / 3

if num1 <= media and num2 <= media and num3 <= media:
    print(0)
if num1 > media and num2 > media or num1 > media and num3 > media or num2 > media and num3 > media:
    print(2)
if num1 > media >= num2 and num3 <= media or num2 > media >= num1 and num3 <= media or num3 > media >= num2 and num1 <= media:
    print(1)
