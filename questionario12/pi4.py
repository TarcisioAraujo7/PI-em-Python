entrada = int(input())


def SerieMiguelito(num):
    if num == 1:
        return 3
    if num % 2 == 0:
        return 4 + SerieMiguelito(num-1)
    else:
        return 1 + SerieMiguelito(num-1)


print(SerieMiguelito(entrada))