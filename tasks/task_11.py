number: int = int(input("Введите целое положительное число: "))

# Решение через цикл for
for i in range(number):
    for j in range(i + 1):
        print(i + 1, end=" ")
    print()

# Решение через цикл while
i = 0
while i < number:
    j = 0
    while j <= i:
        print(i + 1, end=" ")
        j += 1

    i += 1
    print()
