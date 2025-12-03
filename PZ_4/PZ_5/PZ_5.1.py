#Найти сумму чисел ряда 1,2,3,...,60 с использованием функции нахождения суммы. Использовать локальные переменные.
def countInt(k):
    t = 0
    while k > 0:
        k //= 10
        t += 1
    return t
try:
    number = int(input("Введите целое число: "))
    print('Количество цифр в числе:', countInt(number))
except ValueError:
    print("Неправильно ввели!")