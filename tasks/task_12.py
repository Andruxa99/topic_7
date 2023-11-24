# Решение через цикл for
number: int = int(input("Введите целое положительное число: "))
#
# for i in range(number):
#     for j in range(number - i - 1):
#         print(" ", end=" ")
#     for k in range(2 * i + 1):
#         print("*", end=" ")
#     print()

# Решение через цикл while
row: int = 1

while row <= number:
    spaces = number - row
    i = 1
    while i <= spaces:
        print(" ", end=" ")
        i += 1
    i = 1
    while i <= 2 * row - 1:
        print("*", end=" ")
        i += 1
    print()
    row += 1
