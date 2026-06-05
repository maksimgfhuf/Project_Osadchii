"""Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых
положительных и отрицательных чисел. Сформировать новый текстовый файл
 (.txt) следующего вида, предварительно выполнив
 требуемую обработку элементов:"""
import random

numbers = [random.randint(-5, 5) for _ in range(15)]
with open("input.txt", "w", encoding="utf-8") as f:
    f.write(" ".join(map(str, numbers)))

with open("input.txt", "r", encoding="utf-8") as f:
    raw = f.read().split()
    nums = [int(x) for x in raw]

total = len(nums)
neg_odd = [x for x in nums if x < 0 and x % 2 != 0]
sum_neg_odd = sum(neg_odd)
avg_neg_odd = sum_neg_odd / len(neg_odd) if len(neg_odd) > 0 else 0.0

with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Исходные данные: " + " ".join(map(str, nums)) + "\n")
    f.write("Количество элементов: " + str(total) + "\n")
    f.write("Отрицательные нечетные элементы: " + " ".join(map(str, neg_odd)) + "\n")
    f.write("Сумма отрицательных нечетных элементов: " + str(sum_neg_odd) + "\n")
    f.write("Среднее арифметическое отрицательных нечетных элементов: " + str(round(avg_neg_odd, 2)) + "\n")

print("Файлы input.txt и output.txt успешно созданы.")