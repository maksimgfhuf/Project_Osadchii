"""1 Проверить есть ли в последовательности целых N чисел число K."""
def main():
    try:
        n = int(input("Введите количество элементов последовательности (N): "))
        k = int(input("Введите искомое число K: "))
        print("Введите элементы последовательности через пробел:")

        sequence = [int(x) for x in input().split()]
        matches = list(filter(lambda x: x == k, sequence))

        print(f"\n{'='*45}")
        print(f"Исходная последовательность : {sequence}")
        print(f"Искомое число K             : {k}")
        print(f"Найденные совпадения        : {matches}")
        print(f"Результат                   : {' Число K ПРИСУТСТВУЕТ' if matches else ' Число K ОТСУТСТВУЕТ'}")

    except ValueError as e:
        print(f"Ошибка ввода данных: {e}. Убедитесь, что введены целые числа.")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")

