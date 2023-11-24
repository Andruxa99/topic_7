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

print(" ".join(map(str, factors)))
