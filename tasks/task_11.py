# Решение через цикл for
number: int = int(input("Введите целое положительное число: "))

for i in range(number):
    for j in range(i + 1):
        print(i + 1, end=" ")
    print()

# Решение через цикл while
i, j = 0, 0
while i < number:
    while j <= i:
        print(i + 1, end=" ")
        j += 1
    j = 0
    i += 1
    print()
