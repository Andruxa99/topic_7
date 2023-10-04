start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

if start > end:
    start, number_2 = end, start

if start == end:
    if start % 2 == 0:
        print(start)
    else:
        print(0)
else:
    for number in range(start, end+1):
        if number % 2 == 0:
            print(number)
