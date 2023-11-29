n = int(input())

for i in range(n, 0, -1):
    # левый край
    for j in range(i):
        print('x', end='')
    # пробелы
    for j in range(2 * n - 2 * i):
        print(' ', end='')
    # правый край
    for j in range(i):
        print('x', end='')
    print()

for i in range(2, n + 1):
    # левый край
    for j in range(i):
        print('x', end='')
    # пробелы
    for j in range(2 * n - 2 * i):
        print(' ', end='')
    # правый край
    for j in range(i):
        print('x', end='')
    print()
