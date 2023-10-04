# Исходный список чисел
numbers = ["105", "42", "98", "120", "84", "80", "110", "119", "130", "99"]

for number in numbers:
    num = int(number)
    if num > 100 and (num % 5 == 0 or num % 7 == 0):
        print(num, end=" ")
