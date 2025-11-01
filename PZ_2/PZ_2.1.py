#Дано двузначное число.Вывести число , полученное при перестановке цифр исходного числа.

number = int(input("Введите двузначное число: "))

if 10 <= number <= 99:
    tens = number // 10
    units = number % 10

    reversed_number = units * 10 + tens

    print(f"Исходное число: {number}")
    print(f"Число после перестановки цифр: {reversed_number}")
else:
    print("Ошибка! Введите двузначное число.")