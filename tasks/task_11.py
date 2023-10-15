# решение через цикл for

rows: int = int(input())
#
# for i in range(1, rows + 1):
#     for j in range(i):
#         print(i, end=' ')
#     print()

# решение через цикл while

i = 0
j = 0

while i < rows:
    while j <= i:
        print(i + 1, end=' ')
        j += 1
    j = 0
    i += 1
    print('')
