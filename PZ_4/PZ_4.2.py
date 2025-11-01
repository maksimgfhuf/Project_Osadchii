def find_min_k():
    """Находит наименьшее K, для которого сумма 1+2+...+K >= N"""

    N = int(input("Введите целое число N (>1): "))

    if N <= 1:
        print("Ошибка: N должно быть больше 1!")
        return

    K = 0
    total_sum = 0

    while total_sum < N:
        K += 1
        total_sum += K

    print(f"\nНаименьшее K: {K}")
    print(f"Сумма 1 + 2 + ... + {K} = {total_sum}")
    print(f"Условие: {total_sum} >= {N}")

print("=== Поиск наименьшего K ===")
find_min_k()