#Даны три целых числа: A, B, C. Проверить истинность высказывания: «Хотя бы одно из чисел A, B, C положительное».
try:
    numbers = [
        int(input("Введите число A: ")),
        int(input("Введите число B: ")),
        int(input("Введите число C: "))
    ]
    result = any(num > 0 for num in numbers)
    print(result)
except ValueError:
    print("Ошибка! Убедитесь, что вводите целые числа.")
