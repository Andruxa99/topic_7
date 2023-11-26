number: int = int(input("Введите число: "))

# Неправильно, факториал числа 0 равен 1, посмотри на второй тест
if number <= 1:
    print("Факториал определен только для натуральных чисел")
else:
    factorial: int = 1
    for i in range(2, number + 1):
        factorial *= i
    print("Факториал числа", number, "равен", factorial)
