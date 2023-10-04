number = int(input("Введите число: "))

factorial = 1
num = 1

if number < 0:
    print("Факториал определен только для натуральных чисел")
else:
    while num <= number:
        factorial *= num
        num += 1
    print("Факториал числа", number, "равен", factorial)
