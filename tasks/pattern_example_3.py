n = int(input())  # 5

# на первой строке 4 пробела, одна звездочка

for i in range(n, 1, -1):
    # Пробелы
    for j in range(0, i - 1):
        print(' ', end='')

    # Звездочки
    for k in range(n - i + 1):
        print('*', end='')

    print()

# for i in range(...):
#     # Пробелы
#     for j in range(...):
#         ...
#
#     # Звездочки
#     for k in range(...):
#         ...
