start: int = int(input("Введите начало диапазона: "))
end: int = int(input("Введите конец диапазона: "))

if start > end:
    start, end = end, start
for number in range(start, end + 1):
    if number % 2 == 0:
        print(number)
