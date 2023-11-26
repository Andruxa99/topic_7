num_1: int = int(input("Введите число: "))

if num_1 < 1:
    print("Число должно быть больше или равно 1")
elif num_1 == 1:
    print(1)
else:
    total_sum: int = 0
    for i in range(1, num_1 + 1):
        total_sum += i
    print("Сумма всех чисел от 1 до", num_1, "равна", total_sum)
