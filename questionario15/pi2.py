
def verif_email(email):
    saida = True
    pos_arroba = email.index('@')
    if pos_arroba == 0:
        saida = False
    resto_email = email[(pos_arroba+1):].split('.')
    for parte in resto_email:
        if parte == '':
            resto_email.remove(parte)
    if len(resto_email) != 3:
        saida = False
    return saida


while True:
    email_entrada = input()
    if email_entrada == 'sair':
        break
    if verif_email(email_entrada):
        print('certo')
    else:
        print('errado')
