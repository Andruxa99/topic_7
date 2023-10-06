start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

if start > end:
    # 1. Откуда переменная number_2? Где она используеися
    start, number_2 = end, start

# Эти условия должны быть реализованы
# внутри цикла (в цикле будет только if elif)
if start == end:
    if start % 2 == 0:  # Это ты уже реализовал в цикле
        print(start)
    else:
        print(0)
else:
    for number in range(start, end + 1):
        if number % 2 == 0:  # Это правильно
            print(number)
        elif ...:
            ...
