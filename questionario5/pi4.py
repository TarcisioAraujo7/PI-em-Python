lado1 = int(input())
lado2 = int(input())
lado3 = int(input())
lado4 = int(input())


def e_retangulo(l1, l2, l3, l4):
    if l1 == l2 and l3 == l4:
        return True
    elif l1 == l3 and l2 == l4:
        return True
    elif l1 == l4 and l2 == l3:
        return True
    else:
        return False


if e_retangulo(lado1, lado2, lado3, lado4):
    print('RETANGULO')
else:
    print('NAO EH UM RETANGULO')
