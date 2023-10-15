# Решение через цикл for

n = int(input())

# for i in range(n):
#     for j in range(n - i - 1):
#         print(" ", end=" ")
#     for k in range(2 * i + 1):
#         print("*", end=" ")
#     print()

# Решение через цикл while

row = 1
while row <= 4:
    space = 4 - row
    while space > 0:
        print(" ", end=" ")
        space -= 1
    star = (2 * row) - 1
    while star > 0:
        print("*", end=" ")
        star -= 1
    print()
    row += 1
