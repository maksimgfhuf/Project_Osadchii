#Дано вещественное число A и целое число N (>0). Найти A в степени N: AN = AA ... •A (числа A перемножаются N раз).
try:
    A = int(input("Введите число A: "))
    N = int(input("Введите степень N: "))
    if N <= 0:
        print("Ошибка: Степень N должна быть больше нуля!")
    else:
        result = 1
        count = 0
        while count < N:
            result = result * A
            count = count + 1
        print(f"{A} в степени {N} = {result}")
except ValueError:
    print("Ошибка: Введите числа корректно!")
    print("Для A можно вводить: 2, 3.5, -1.2")

    print("Для N можно вводить: 1, 5, 10 (только целые положительные числа)")
