# # Решение через цикл for
number: int = int(input("Введите целое положительное число: "))

# for i in range(number, 0, -1):
#     for j in range(number - i):
#         print(" ", end="")
#     for j in range(2 * i - 1):
#         print("*", end="")
#     print()
#
# for i in range(2, number + 1):
#     for j in range(number - i):
#         print(" ", end="")
#     for j in range(2 * i - 1):
#         print("*", end="")
#     print()
# Решение через цикл while
i: int = 1
while i <= number:
    j: int = 1
    while j < i:
        print(" ", end="")
        j += 1
    j = 2 * number - 2 * i + 1
    while j > 0:
        print("*", end="")
        j -= 1
    print()
    i += 1

i = number - 1
while i >= 1:
    j = 1
    while j < i:
        print(" ", end="")
        j += 1
    j = 2 * number - 2 * i + 1
    while j > 0:
        print("*", end="")
        j -= 1
    print()
    i -= 1
