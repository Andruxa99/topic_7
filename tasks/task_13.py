number: int = int(input("Введите целое положительное число: "))

# Решение через цикл for
count = 1
for i in range(1, number + 1):
    for j in range(i):
        print(count, end=" ")
        count += 1
    print()
