number: int = int(input("Введите число: "))

if number < 1:
    print("Число должно быть больше или равно 1")
elif number == 1:
    print(1)
else:
    # Создадим summa и num по необходимости.
    # Нет смысла создавать эти переменные выше,
    # если введенное число будет меньше 0 или равна 1,
    # то они не будут использоваться
    summa: int = 0
    num: int = 1
    while num <= number:
        summa += num
        num += 1
    print("Сумма всех чисел от 1 до", number, "равна:", summa)

# Браво! Все круто!
