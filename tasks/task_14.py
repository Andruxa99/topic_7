# # Решение через цикл for
number: int = int(input("Введите целое положительное число: "))
# Верхняя часть
# for i in range(number, 0, -1):
#     for j in range(0, number - i):
#         print(" ", end="")
#     for k in range(2 * i - 1):
#         print("*", end="")
#     print()
# Нижняя часть
# for i in range(2, number + 1):
#     for j in range(number - i):
#         print(" ", end="")
#     for k in range(2 * i - 1):
#         print("*", end="")
#     print()

# Решение через цикл while
# Верхняя часть
row_1: int = number
while row_1 >= 1:
    spaces = number - row_1
    while spaces > 0:
        print(" ", end="")
        spaces -= 1
    stars = 2 * row_1 - 1
    while stars > 0:
        print("*", end="")
        stars -= 1
    print()
    row_1 -= 1

# Нижняя часть
row = 2
while row <= number:
    spaces = number - row
    while spaces > 0:
        print(" ", end="")
        spaces -= 1
    stars = 2 * row - 1
    while stars > 0:
        print("*", end="")
        stars -= 1
    print()
    row += 1
