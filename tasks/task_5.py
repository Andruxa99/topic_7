number: int = int(input("Введите число: "))

factorial: int = 1

if number <= 1:
    print("Факториал определен только для натуральных чисел")
else:
    for i in range(2, number + 1):
        factorial *= i
    print("Факториал числа", number, "равен", factorial)

