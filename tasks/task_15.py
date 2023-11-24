# Решение через цикл for
num: int = int(input("Введите целое положительное число: "))
# Верхняя часть ромба
for i in range(1, num + 1):
    print(" " * (num - i), end="")
    print("*" * (2 * i - 1))
#
# # Нижняя часть ромба
for i in range(num - 1, 0, -1):
    print(" " * (num - i), end="")
    print("*" * (2 * i - 1))

# Решение через цикл while

i = 1
spaces = num - 1
stars = 1

# Верхняя часть
while spaces >= 0:
    print(" " * spaces + "*" * stars)
    spaces -= 1
    stars += 2

# Нижняя часть
spaces = 1
stars -= 4
while spaces <= num - 1:
    print(" " * spaces + "*" * stars)
    spaces += 1
    stars -= 2
