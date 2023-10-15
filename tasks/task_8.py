start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

for number in range(start, end + 1):
    if start > end:
        start, end = end, start

    if start == end:
        if start % 2 == 0:
            print(start)
        else:
            print(0)
    if number % 2 == 0:
        print(number)
