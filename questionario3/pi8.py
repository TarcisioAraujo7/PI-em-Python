ano = int(input())
div4 = (int(ano / 4) * 4) == ano
div100 = (int(ano / 100) * 100) == ano
div400 = (int(ano / 400) * 400) == ano

if not div4 or div4 and div100 and not div400:
    print('NAOBISSEXTO')
else:
    print('BISSEXTO')
