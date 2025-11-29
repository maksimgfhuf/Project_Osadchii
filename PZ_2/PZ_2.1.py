#Дано двузначное число.Вывести число , полученное при перестановке цифр исходного числа.
try:
    n = int(input("введите двузначное число: "))

    if 10 <= n <= 99:

        first_digit = n // 10

        second_digit = n % 10

        reversed_number = second_digit * 10 + first_digit

        print("число после перестановки:", reversed_number)
    else:

        print("ошибка: введите именно двузначное число")
except ValueError:

    print("ошибка: введите целое число")
