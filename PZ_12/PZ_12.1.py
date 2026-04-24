"""1. Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее элементов."""
import random

try:
    rows = int(input("Количество строк: "))
    cols = int(input("Количество столбцов: "))

    matrix = [[random.randint(1, 20) for _ in range(cols)] for _ in range(rows)]

    print("Исходная матрица:")
    for row in matrix:
        print(' '.join(map(str, row)))

    if not matrix:
        print("Матрица пуста.")
    elif cols == 0:
        print("Ошибка: количество столбцов должно быть больше нуля.")
    else:

        result = [
            sum(row) / len(row)
            for i, row in enumerate(matrix)
            if (i + 1) % 2 != 0
        ]

        print("\nСреднее арифметическое элементов строк с нечетными номерами:")
        print('\n'.join(f"Строка {idx * 2 + 1}: {val:.2f}" for idx, val in enumerate(result)))
except ValueError:
    print("Ошибка: введите корректные целые числа.")