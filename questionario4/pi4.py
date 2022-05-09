alice = int(input())
beto = int(input())
clara = int(input())

if alice != beto and alice != clara:
    print('A')
elif beto != alice and beto != clara:
    print('B')
elif clara != alice and clara != beto:
    print('C')
else:
    print('*')
