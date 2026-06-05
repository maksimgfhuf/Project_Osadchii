"""2. В матрице найти максимальный положительный элемент, кратный 4"""
import random

try:
    rows, cols = int(input("Количество строк: ")), int(input("Количество столбцов: "))
    matrix = [[random.randint(-20, 20) for _ in range(cols)] for _ in range(rows)]

    print("Исходная матрица:")
    print(''.join(' '.join(map(str, row)) for row in matrix))

    max_val = max((x for row in matrix for x in row if x > 0 and x % 4 == 0), default=None)

    print(
        f"Результат: {'Максимальный положительный элемент, кратный 4: ' + str(max_val) if max_val else 'В матрице отсутствуют положительные элементы, кратные 4.'}")

except ValueError:
    print("Ошибка: введите корректные целые числа.")