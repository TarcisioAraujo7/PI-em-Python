duracao = int(input())

horas = int(duracao/3600)
duracao = duracao - int(horas) * 3600

minutos = int(duracao/60)
duracao = duracao - int(minutos) * 60

print(str(horas) + ':' + str(minutos) + ':' + str(duracao))
