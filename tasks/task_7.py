number: int = int(input("Введите число: "))

# список для хранения простых множителей
factors: list = []

# поиск простых множителей числа
divider: int = 2
while number > 1:
    if number % divider == 0:
        factors.append(divider)
        number //= divider
    else:
        divider += 1

# Можно было сразу вывести в цикле
# print(" ".join(map(str, factors)))

# Или использовать оператор распаковки *
print(*factors)

# Хорошее решение!
