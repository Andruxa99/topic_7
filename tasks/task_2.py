# Решение через for
num_1: int = int(input("Введите число: "))
print("Таблица умножения для числа", num_1, "с помощью цикла for:")
for i in range(1, 11):
    print(num_1, "*", i, "=", num_1 * i)

# Решение через while
print("Таблица умножения для числа", num_1, "с помощью цикла while:")
count: int = 1
while count <= 10:
    print(num_1, "*", count, "=", num_1 * count)
    count += 1
