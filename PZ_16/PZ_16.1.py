#Создайте класс Кмпьютер с атрибутами марка, процессор и оперативная память.
# Напишите метод, который выводит информацию о компьютере в формате Марка: марка, Процессор: процессор, Оперативная память: память"
class Computer:

    def __init__(self, marka: str, processor: str, ram: str):

        self.marka = marka
        self.processor = processor
        self.ram = ram

    def display_info(self) -> str:

        print( f"Марка: {self.marka}, Процессор: {self.processor}, Оперативная память: {self.ram}")

print(" Тестирование класса Computer ")

pc1 = Computer("ASUS", "Intel Core i5-12400F", "16 ГБ DDR4")
pc1.display_info()

pc2 = Computer("MSI", "AMD Ryzen 7 5800X", "32 ГБ DDR4")
pc2.display_info()
