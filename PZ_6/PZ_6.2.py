#Дано число R и список размера N. Найти два соседних элемента списка, суммакоторых наиболее близка к числу R, и вывести эти элементы в порядке возрастания их индексов (определение наиболее близких чисел - то есть такой элемент AK, для которого величина |AK - R| является минимальной).
try:
    R = float(input("Введите число R: "))
    N = int(input("Введите размер списка N: "))
    if N < 2:
        print("Ошибка: нужно минимум 2 элемента")
    else:
        lst = []
        for i in range(N):
            lst.append(float(input(f"Элемент {i + 1}: ")))
        min_diff = float('inf')
        best_i = 0
        for i in range(N - 1):
            diff = abs(lst[i] + lst[i + 1] - R)
            if diff < min_diff:
                min_diff = diff
                best_i = i
        print("Исходный список:", lst)
        print(f"Элементы: {lst[best_i]} и {lst[best_i + 1]}")
        print(f"Индексы: {best_i} и {best_i + 1}")
except ValueError:
    print("Ошибка ввода!")