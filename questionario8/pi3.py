def traduzir(codigo):
    traducao = ''
    tabela = ' abcdefghijklmnopqrstuvwxyz'
    for digito in codigo:
        traducao = traducao + tabela[int(digito)]
    return traducao


while True:
    mensagem = input()
    msg_formatada = mensagem.split()
    if traduzir(msg_formatada) == 'fim':
        break
    else:
        print(traduzir(msg_formatada))
