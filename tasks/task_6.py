number: int = abs(int(input("Введите целое число: ")))

count: int = 0
while number > 0:
    number //= 10
    count += 1
print("Количество  цифр в числе:", count)
