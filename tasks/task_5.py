number: int = int(input("Введите число: "))

if number < 0:
    print("Факториал определен только для натуральных чисел")
else:
    factorial: int = 1
    num: int = 1
    while num <= number:
        factorial *= num
        num += 1
    print("Факториал числа", number, "равен", factorial)

# Все отлично!
# Не забываем про аннотация типа.
