# Способ 1-ый
num_1 = int(input("Введите число: "))

total = 0

# for i in range(1, 11):
#     total = num_1 * i
#     print("Таблица умножения для числа", num_1,
#           "с помощью цикла for:", num_1, "*", i, "=", total)

# Способ 2-ой

j = 1
while j <= 10:
    total = num_1 * j
    print("Таблица умножения для числа", num_1,
          "с помощью цикла while:", num_1, "*", j, "=", total)
    j += 1

