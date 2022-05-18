num1 = float(input())
num2 = float(input())
operacao = input()


def operacoes(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1 / n2


resultado = operacoes(num1, num2, operacao)
print('%4.3f' % resultado)

while True:
    num1 = float(input())
    operacao = input()
    if operacao == '&':
        break
    elif operacao == '/' and num1 == 0:
        print('operacao nao pode ser realizada')
    else:
        resultado = operacoes(resultado, num1, operacao)
        print('%4.3f' % resultado)
