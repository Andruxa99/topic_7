number = int(input("Введите число: "))

summa = 0
num = 1

if number < 1:
    print("Число должно быть больше или равно 1")
elif number == 1:
    print(1)
else:
    while num <= number:
        summa += num
        num += 1
    print("Сумма всех чисел от 1 до", number, "равна:", summa)
