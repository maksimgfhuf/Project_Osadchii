"В строках исходного текстового файла (dates1.txt) все даты представить в виде подстроки. Поместить в новый текстовый файл все даты февраля в формате ДД/ММ/ГГГГ"
import re
try:
    with open("dates1.txt", 'r', encoding='utf-8') as f:
        text = f.read()
    dates = re.findall(r'\b(\d{2})\.(\d{2})\.(\d{4})\b', text)
    february_dates = []
    for day, month, year in dates:
        if month == '02':
            february_dates.append(f"{day}/{month}/{year}")
    with open("february_dates.txt", 'w', encoding='utf-8') as f:
        if february_dates:
            for date in february_dates:
                f.write(date + '\n')
            print(f"Найдено {len(february_dates)} дат февраля. Результат сохранён в 'february_dates.txt'")
        else:
            f.write("Даты февраля не найдены")
            print("Даты февраля не найдены")
except FileNotFoundError:
    print("Файл 'dates1.txt' не найден")
except Exception as e:
    print(f"Ошибка: {e}")