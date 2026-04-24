#Дана строка. Подсчитать количество содержащихся в ней цифр.
try:
    s = input("Введите строку: ")
    count = 0
    for char in s:
        if char.isdigit():
            count += 1
    print(f"Количество цифр: {count}")
except Exception:
    print("Произошла ошибка при обработке строки")