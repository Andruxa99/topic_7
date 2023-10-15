number: int = int(input("Введите целое число: "))

number: int = abs(number)  # перевод числа в абсолютное значение

count = 0
while number > 0:
    count += 1
    number //= 10  # удаляем последнюю цифру
print("Количество цифр в числе:", count)
