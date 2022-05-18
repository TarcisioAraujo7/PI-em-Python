nome = {}
mensalidade = {}

for _ in range(100):
    name = input()
    if name == 'SAIR':
        break
    senha = int(input())
    situacao_mensalidade = input()
    nome[senha] = name
    mensalidade[senha] = situacao_mensalidade

while True:
    codigo = int(input())
    if codigo == -1:
        break
    if codigo not in nome:
        print('Seja bem-vindo(a)! Procure a recepção!')
    elif mensalidade[codigo] == 'P':
        print(nome[codigo] + ', seja bem-vindo(a)!')
    else:
        print('Não está esquecendo de algo,', nome[codigo] + '? Procure a recepção!')
