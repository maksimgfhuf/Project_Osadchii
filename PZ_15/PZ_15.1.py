"Приложение ТОВАРНЫЙ ЗАПАС для автоматизированного учета товарных запасов на складе. БД должна содержать таблицу Товары со следующей структурой записи: Код товара, Торговая марка, Тип, Цена, Количество на складе, Минимальный запас."
import sqlite3

DB_NAME = "warehouse.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    conn.commit()
    return conn

def add_test_data(conn):

    data = [
        ("Samsung", "Телевизор", 45990, 15, 5), ("LG", "Холодильник", 32500, 8, 3),
        ("Bosch", "Стиральная машина", 28900, 12, 4), ("Apple", "Ноутбук", 89990, 5, 2),
        ("Xiaomi", "Смартфон", 25490, 20, 10), ("Sony", "Наушники", 8990, 30, 15),
        ("Philips", "Кофеварка", 12500, 10, 5), ("Dell", "Монитор", 18750, 7, 3),
        ("HP", "Принтер", 15200, 6, 2), ("Canon", "Фотоаппарат", 42300, 4, 2)]
    conn.executemany("INSERT INTO Товары VALUES (NULL,?,?,?,?,?)", data)
    conn.commit()
    print("10 тестовых записей добавлено.")

def search_brand(conn, val): return conn.execute("SELECT * FROM Товары WHERE brand LIKE ?", (f"%{val}%",)).fetchall()
def search_type(conn, val): return conn.execute("SELECT * FROM Товары WHERE product_type LIKE ?", (f"%{val}%",)).fetchall()
def search_low(conn): return conn.execute("SELECT * FROM Товары WHERE quantity < min_stock").fetchall()

def delete_code(conn, code): conn.execute("DELETE FROM Товары WHERE product_code = ?", (code,)); conn.commit()
def delete_brand(conn, brand): conn.execute("DELETE FROM Товары WHERE brand = ?", (brand,)); conn.commit()
def delete_zero(conn): conn.execute("DELETE FROM Товары WHERE quantity = 0"); conn.commit()

def update_price(conn, code, val): conn.execute("UPDATE Товары SET price = ? WHERE product_code = ?", (val, code)); conn.commit()
def update_qty(conn, code, val): conn.execute("UPDATE Товары SET quantity = ? WHERE product_code = ?", (val, code)); conn.commit()
def update_min(conn, code, val): conn.execute("UPDATE Товары SET min_stock = ? WHERE product_code = ?", (val, code)); conn.commit()

def show_table(rows):
    if not rows: print(" Нет данных."); return
    print(f"{'Код':<4} {'Марка':<10} {'Тип':<18} {'Цена':>8} {'Кол':>5} {'Мин':>4}")
    for r in rows: print(f"{r[0]:<4} {r[1]:<10} {r[2]:<18} {r[3]:>8.2f} {r[4]:>5} {r[5]:>4}")
def main():
    conn = init_db()

    menu = [
        "1. Все товары",
        "2. Добавить товар",
        "3. Добавить 10 тестовых записей",
        "4. Поиск по марке",
        "5. Поиск по типу",
        "6. Показать товары ниже мин. запаса",
        "7. Изменить цену",
        "8. Изменить количество",
        "9. Изменить мин. запас",
        "10. Удалить по коду",
        "11. Удалить по марке",
        "12. Удалить товары с нулевым остатком",
        "0. Выход"
    ]
    while True:
        print(" ТОВАРНЫЙ ЗАПАС")
        for item in menu:
            print(item)
        ch = input("> ").strip()
        try:
            if ch == "1": show_table(conn.execute("SELECT * FROM Товары").fetchall())
            elif ch == "2":
                conn.execute("INSERT INTO Товары VALUES (NULL,?,?,?,?,?)",
                             (input("Марка: "), input("Тип: "), float(input("Цена: ")),
                              int(input("Кол-во: ")), int(input("Мин.запас: "))))
                conn.commit(); print(" Добавлено")
            elif ch == "3": add_test_data(conn)
            elif ch == "4": show_table(search_brand(conn, input("Марка: ")))
            elif ch == "5": show_table(search_type(conn, input("Тип: ")))
            elif ch == "6": show_table(search_low(conn))
            elif ch == "7": update_price(conn, int(input("Код: ")), float(input("Цена: ")));
            elif ch == "8": update_qty(conn, int(input("Код: ")), int(input("Кол-во: ")));
            elif ch == "9": update_min(conn, int(input("Код: ")), int(input("Мин: ")));
            elif ch == "10": delete_code(conn, int(input("Код: "))); print(" Удалено")
            elif ch == "11": delete_brand(conn, input("Марка: ")); print(" Удалено")
            elif ch == "12": delete_zero(conn); print(" Удалены нулевые")
            elif ch == "0": conn.close(); break
        except ValueError:
            print(" Ошибка: введите корректное число.")
        except Exception as e:
            print(f" Ошибка БД: {e}")

main()