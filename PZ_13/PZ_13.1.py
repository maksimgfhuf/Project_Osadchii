#В строках исходного текстового файла (dates1.txt) все даты представить в виде подстроки. Поместить в новый текстовый
# файл все даты февраля в формате ДД/ММ/ГГГГ"
import re

try:

    with open("dates1.txt", 'r', encoding='utf-8') as f:
        text = f.read()

    february_substrings = re.findall(r'\b\d{2}\.02\.\d{4}\b', text)

    formatted_dates = [date.replace('.', '/') for date in february_substrings]

    with open("february_dates.txt", 'w', encoding='utf-8') as f:
        if formatted_dates:
            for date in formatted_dates:
                f.write(date + '\n')
            print(f"Найдено {len(formatted_dates)} дат февраля. Результат сохранён в 'february_dates.txt'")
        else:
            f.write("Даты февраля не найдены\n")
            print("Даты февраля не найдены")

except FileNotFoundError:
    print("Файл 'dates1.txt' не найден. Создайте его в папке со скриптом.")
except Exception as e:
    print(f"Произошла ошибка: {e}")