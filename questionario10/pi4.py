quantidade = int(input())
entrada_str = input()
entrada_list = entrada_str.split()
contador = 0
saida1 = ''
saida2 = entrada_list.copy()
saida3 = entrada_list.copy()
saida3.sort()
saida3.reverse()


def list_str(entrada):
    string = ''
    for num in entrada:
        string = string + num
    return ' '.join(string)


for numero in entrada_str:
    saida1 = numero + saida1

for numero in entrada_list:
    saida2.insert(contador-1, numero)
    saida2.pop(contador)

saida2.insert(-1, entrada_list[0])
saida2.pop(-1)

saida3.sort()
saida3.reverse()

print(saida1)
print(list_str(saida2))
print(list_str(saida3))
