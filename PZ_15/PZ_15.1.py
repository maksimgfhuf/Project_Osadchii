#Приложение ТОВАРНЫЙ ЗАПАС для автоматизированного учета товарных
#запасов на складе. БД должна содержать таблицу Товары со следующей структурой записи:
#Код товара, Торговая марка, Тип, Цена, Количество на складе, Минимальный запас.
import sqlite3
from data import TEST_DATA

DB_NAME = "warehouse.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("""CREATE TABLE IF NOT EXISTS Товары (
        product_code INTEGER PRIMARY KEY AUTOINCREMENT,
        brand TEXT NOT NULL, product_type TEXT NOT NULL,
        price REAL CHECK(price >= 0), quantity INTEGER CHECK(quantity >= 0),
        min_stock INTEGER CHECK(min_stock >= 0))""")
    conn.commit()
    return conn


def add_test_data(conn):
    conn.executemany("INSERT INTO Товары VALUES (NULL,?,?,?,?,?)", TEST_DATA)
    conn.commit()
    print("10 тестовых записей добавлено.")


def search_brand(conn, val):
    return conn.execute("SELECT * FROM Товары WHERE brand LIKE ?", (f"%{val}%",)).fetchall()


def search_type(conn, val):
    return conn.execute("SELECT * FROM Товары WHERE product_type LIKE ?", (f"%{val}%",)).fetchall()


def search_low(conn):
    return conn.execute("SELECT * FROM Товары WHERE quantity < min_stock").fetchall()


def delete_code(conn, code):
    conn.execute("DELETE FROM Товары WHERE product_code = ?", (code,))
    conn.commit()


def delete_brand(conn, brand):
    conn.execute("DELETE FROM Товары WHERE brand = ?", (brand,))
    conn.commit()


def delete_zero(conn):
    conn.execute("DELETE FROM Товары WHERE quantity = 0")
    conn.commit()


def update_price(conn, code, val):
    conn.execute("UPDATE Товары SET price = ? WHERE product_code = ?", (val, code))
    conn.commit()


def update_qty(conn, code, val):
    conn.execute("UPDATE Товары SET quantity = ? WHERE product_code = ?", (val, code))
    conn.commit()


def update_min(conn, code, val):
    conn.execute("UPDATE Товары SET min_stock = ? WHERE product_code = ?", (val, code))
    conn.commit()


def show_table(rows):
    if not rows:
        print(" Нет данных.")
        return
    print(f"{'Код':<4} {'Марка':<10} {'Тип':<18} {'Цена':>8} {'Кол':>5} {'Мин':>4}")
    for r in rows:
        print(f"{r[0]:<4} {r[1]:<10} {r[2]:<18} {r[3]:>8.2f} {r[4]:>5} {r[5]:>4}")


def main():
    conn = init_db()

    menu = [
        "1. Показать все товары",
        "2. Добавить новый товар",
        "3. Загрузить тестовые данные",
        "4. Поиск (по марке или типу)",
        "5. Отчет: товары ниже мин. запаса",
        "6. Изменить цену товара",
        "7. Изменить остатки (кол-во / мин. запас)",
        "8. Удалить товар (по коду или марке)",
        "9. Удалить товары с нулевым остатком",
        "0. Выход"
    ]

    while True:
        print("\n ТОВАРНЫЙ ЗАПАС")
        for item in menu:
            print(item)
        ch = input("> ").strip()

        try:
            if ch == "1":
                show_table(conn.execute("SELECT * FROM Товары").fetchall())

            elif ch == "2":
                conn.execute("INSERT INTO Товары VALUES (NULL,?,?,?,?,?)",
                             (input("Марка: "), input("Тип: "), float(input("Цена: ")),
                              int(input("Кол-во: ")), int(input("Мин.запас: "))))
                conn.commit()
                print(" Добавлено")

            elif ch == "3":
                add_test_data(conn)

            elif ch == "4":
                sub = input("1-по марке, 2-по типу > ").strip()
                if sub == "1":
                    show_table(search_brand(conn, input("Марка: ")))
                elif sub == "2":
                    show_table(search_type(conn, input("Тип: ")))
                else:
                    print(" Неверный выбор")

            elif ch == "5":
                show_table(search_low(conn))

            elif ch == "6":
                code = int(input("Код товара: "))
                update_price(conn, code, float(input("Новая цена: ")))
                print(" Цена обновлена")

            elif ch == "7":
                code = int(input("Код товара: "))
                sub = input("1-Кол-во, 2-Мин.запас > ").strip()
                if sub == "1":
                    update_qty(conn, code, int(input("Новое кол-во: ")))
                    print(" Количество обновлено")
                elif sub == "2":
                    update_min(conn, code, int(input("Новый мин. запас: ")))
                    print(" Мин. запас обновлен")
                else:
                    print(" Неверный выбор")

            elif ch == "8":
                sub = input("1-по коду, 2-по марке > ").strip()
                if sub == "1":
                    delete_code(conn, int(input("Код: ")))
                    print(" Удалено")
                elif sub == "2":
                    delete_brand(conn, input("Марка: "))
                    print(" Удалено")
                else:
                    print(" Неверный выбор")

            elif ch == "9":
                delete_zero(conn)
                print(" Удалены товары с нулевым остатком")

            elif ch == "0":
                conn.close()
                break
            else:
                print(" Неверный выбор, попробуйте снова.")

        except ValueError:
            print(" Ошибка: введите корректное число.")
        except Exception as e:
            print(f" Ошибка БД: {e}")


main()