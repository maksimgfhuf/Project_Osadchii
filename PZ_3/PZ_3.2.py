def is_leap_year(year):
    """Проверяет, является ли год високосным"""
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

def get_days_in_year(year):
    """Возвращает количество дней в году"""
    return 366 if is_leap_year(year) else 365

year = int(input("Введите год: "))

if year <= 0:
    print("Год должен быть положительным числом!")
else:
    days = get_days_in_year(year)
    leap_status = "високосный" if is_leap_year(year) else "обычный"
    print(f"В году {year} - {days} дней ({leap_status})")