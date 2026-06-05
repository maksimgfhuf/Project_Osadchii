"""1. Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее элементов."""
import random

try:
    rows, cols = int(input("Строки: ")), int(input("Столбцы: "))
    if rows <= 0 or cols <= 0: raise ValueError

    matrix = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]
    print("Исходная матрица:")
    print(''.join(' '.join(map(str, row)) for row in matrix))

    result = map(
        lambda i_row: f"Строка {i_row[0]}: {sum(i_row[1]) / len(i_row[1]):.2f}",
        filter(lambda i_row: i_row[0] % 2 != 0, enumerate(matrix, start=1))
    )

    print("Среднее арифметическое строк с нечетными номерами:")
    print(''.join(result) or "Нет строк с нечётными номерами.")

except ValueError:
    print("Ошибка: введите корректные положительные целые числа.")