start: int = int(input("Введите начало диапазона: "))
end: int = int(input("Введите конец диапазона: "))

if start > end:
    start, end = end, start

if start < 0 or end < 0 or start == end:
    print("Некорректный диапазон")
else:
    for num in range(start, end + 1):
        digits = str(num)
        power = len(digits)
        sum_of_powers = 0

        for digit in digits:
            sum_of_powers += int(digit) ** power
        if num == sum_of_powers:
            print(num, end=" ")
