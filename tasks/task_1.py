# Способ 1-ый
print("Решение с использованием цикла for:")
for num in range(-10, 0):
    print(num)

# Способ 2-ой
print("Решение с использованием цикла while:")
num = -10
while num <= -1:
    print(num)
    num += 1
print()

# Вывод в одну строку
# Способ 2-ой
print("Решение с использованием цикла while:", end=" ")
num = -10
while num <= -1:
    print(num, end=" ")
    num += 1
print()
