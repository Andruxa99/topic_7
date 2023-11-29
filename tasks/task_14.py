# # Решение через цикл for
number: int = int(input("Введите целое положительное число: "))

for i in range(number, 0, -1):
    for j in range(0, number - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

for i in range(2, number + 1):
    for j in range(number - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
