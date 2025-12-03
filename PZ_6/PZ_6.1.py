#Дан список A размера N. Вывести вначале его элементы с четными номерами (в порядке возрастания номеров), а затем — элементы с нечетными номерами (также в порядке возрастания номеров): A2, A4, А6, . . ., A1, A3, A5, ... . Условный оператор не использовать.
try:
    N = int(input("Введите размер списка N: "))
    A = []
    for i in range(N):
        A.append(int(input(f"Введите элемент A[{i}]: ")))
    print("Исходный список:", A)
    even_index_elements = []
    i = 1
    while i < N:
        even_index_elements.append(A[i])
        i += 2
    odd_index_elements = []
    i = 0
    while i < N:
        odd_index_elements.append(A[i])
        i += 2
    result = even_index_elements + odd_index_elements
    print("Результирующий список:", result)
except ValueError:
    print("Ошибка: введите целые числа!")
