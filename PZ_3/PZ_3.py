def check_positive_numbers(a, b, c):
    """Проверяет, является ли истинным высказывание
    'Хотя бы одно из чисел A, B, C положительное'"""
    return a > 0 or b > 0 or c > 0

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
C = int(input("Введите число C: "))

result = check_positive_numbers(A, B, C)
print(f"Результат: {result}")