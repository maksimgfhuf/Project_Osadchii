"""2. В матрице найти максимальный положительный элемент, кратный 4"""
import random
try:
    rows = int(input("Количество строк: "))
    cols = int(input("Количество столбцов: "))

    matrix = [[random.randint(-20, 40) for _ in range(cols)] for _ in range(rows)]

    print("\nИсходная матрица:")
    for row in matrix:
        print(' '.join(map(str, row)))

    positive_multiples_4 = (x for row in matrix for x in row if x > 0 and x % 4 == 0)
    max_element = max(positive_multiples_4, default=None)

    if max_element is not None:
        print(f"\nМаксимальный положительный элемент, кратный 4: {max_element}")
    else:
        print("\nВ матрице отсутствуют положительные элементы, кратные 4.")

except ValueError:
    print("Ошибка: введите корректные целые числа.")