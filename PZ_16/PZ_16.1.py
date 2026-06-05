"Создайте класс Кмпьютер с атрибутами марка, процессор и оперативная память. Напишите метод, который выводит информацию о компьютере в формате Марка: марка, Процессор: процессор, Оперативная память: память"
class Computer:

    def __init__(self, marka: str, processor: str, ram: str):

        self.marka = marka
        self.processor = processor
        self.ram = ram

    def display_info(self) -> str:

        return f"Марка: {self.marka}, Процессор: {self.processor}, Оперативная память: {self.ram}"

print(" Тестирование класса Computer ")

pc1 = Computer("ASUS", "Intel Core i5-12400F", "16 ГБ DDR4")
print("Тест 1:", pc1.display_info())

pc2 = Computer("MSI", "AMD Ryzen 7 5800X", "32 ГБ DDR4")
print("Тест 2:", pc2.display_info())

pc3 = Computer("Apple", "Apple M2", "8 ГБ Unified Memory")
print("Тест 3:", pc3.display_info())

pc4 = Computer("Lenovo", "Intel Core i3", "4 ГБ")
print("Тест 4 (до изменения):", pc4.display_info())
pc4.ram = "8 ГБ"
print("Тест 4 (после изменения):", pc4.display_info())

print(" Все тестовые запуски завершены ")