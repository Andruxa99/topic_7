# Решение через цикл for
number: int = int(input("Введите целое положительное число: "))
# count = 1
#
# for i in range(1, number + 1):
#     for j in range(i):
#         print(count, end=" ")
#         count += 1
#     print()

# Решение через цикл while
i: int = 1
count: int = 1
while i <= number:
    j = 1
    while j <= i:
        print(count, end=" ")
        count += 1
        j += 1
    print()
    i += 1
