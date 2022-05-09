tipo_media = input()
valor1 = int(input())
valor2 = int(input())
valor3 = int(input())
media_aritimetica = (valor1 + valor2 + valor3)/3
media_harmonica = 3/((1/valor1)+(1/valor2)+(1/valor3))
media_geometrica = (valor1 * valor2 * valor3)**(1/3)

if tipo_media == 'A':
    print('%4.3f' % media_aritimetica)

if tipo_media == 'H':
    print('%4.3f' % media_harmonica)

if tipo_media == 'G':
    print('%4.3f' % media_geometrica)
