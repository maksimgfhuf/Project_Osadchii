"""1 Проверить есть ли в последовательности целых N чисел число K."""
import random

n, k = map(int, (input("N: "), input("K: ")))

seq = [random.randint(-10, 10) for _ in range(n)]

is_found = any(x == k for x in iter(seq))

print(f"Исходная: {seq}\nРезультат: {is_found}")