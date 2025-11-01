def power_comparison():
    """Сравнение собственной реализации с встроенной функцией"""

    A = float(input("Введите вещественное число A: "))
    N = int(input("Введите целое число N (>0): "))

    if N <= 0:
        print("Ошибка: N должно быть больше 0!")
        return

    custom_result = 1
    for i in range(N):
        custom_result *= A

    builtin_result = A ** N

    print(f"\nСобственная реализация: {A}^{N} = {custom_result}")
    print(f"Встроенная функция pow(): {A}^{N} = {builtin_result}")
    print(f"Результаты совпадают: {custom_result == builtin_result}")

power_comparison()