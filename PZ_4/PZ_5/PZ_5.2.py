#Описать функцию ShiftRight3(A, B, C), выполняющую правый циклический сдвиг: значение A переходит в B, значение B — в C, значение C — в A (A, B, C — вещественные параметры, являющиеся одновременно входными и выходными). С помощью этой функции выполнить правый циклический сдвиг для двух данных наборов из трех чисел: (A1, B1, C1) и (A2, B2, C2).
def ShiftRight3(A, B, C):
    A, B, C = B, C, A
    return A, B, C
try:
    A1 = float(input("Введите A1: "))
    B1 = float(input("Введите B1: "))
    C1 = float(input("Введите C1: "))

    A2 = float(input("Введите A2: "))
    B2 = float(input("Введите B2: "))
    C2 = float(input("Введите C2: "))

    A1, B1, C1 = ShiftRight3(A1, B1, C1)
    A2, B2, C2 = ShiftRight3(A2, B2, C2)

    print("После сдвига:")
    print(f"A1 = {A1}, B1 = {B1}, C1 = {C1}")
    print(f"A2 = {A2}, B2 = {B2}, C2 = {C2}")
except ValueError:
    print("Ошибка: введите числовые значения")