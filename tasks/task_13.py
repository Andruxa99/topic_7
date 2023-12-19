number: int = int(input("Введите целое положительное число: "))

# Решение через цикл for
# count: int = 1
# for i in range(1, number + 1):
#     for j in range(i):
#         print(count, end=" ")
#         count += 1
#     print()

# Решение через while
i: int = 1
count: int = 1
while i < number + 1:
    j: int = 1
    while j <= i:
        print("*", end=" ")
        j += 1
        count += 1

    i += 1
    print()
