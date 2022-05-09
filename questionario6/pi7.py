seg = float(input())
ter = float(input())
qua = float(input())
qui = float(input())
sex = float(input())
sab = float(input())
dom = float(input())

total = seg + ter + qua + qui + sex + sab + dom
diasmeta = 0

while True:
    if ter - seg >= 0.5:
        diasmeta = diasmeta + 1
    if qua - ter >= 0.5:
        diasmeta = diasmeta + 1
    if qui - qua >= 0.5:
        diasmeta = diasmeta + 1
    if sex - qui >= 0.5:
        diasmeta = diasmeta + 1
    if sab - sex >= 0.5:
        diasmeta = diasmeta + 1
    if dom - sab >= 0.5:
        diasmeta = diasmeta + 1
    break

print('R$', '%3.2f' % total)
print(diasmeta)
