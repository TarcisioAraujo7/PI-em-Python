numero = int(input())

if numero == 0:
    print('NULO')
elif numero > 0:
    if numero % 2 == 0:
        print('POSITIVO PAR')
    else:
        print('POSITIVO IMPAR')
else:
    if numero % 2 == 0:
        print('NEGATIVO PAR')
    else:
        print('NEGATIVO IMPAR')
