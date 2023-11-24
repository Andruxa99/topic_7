# Исходный список чисел
numbers: list = ["105", "42", "98", "120", "84",
                 "80", "110", "119", "130", "99"]
print("Числа кратные 5 или 7 больше 100:", end=" ")
for num in numbers:
    num = int(num)
    if num % 5 == 0 or num % 7 == 0:
        if num > 100:
            print(num, end=" ")
