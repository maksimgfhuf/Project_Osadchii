"Создайте базовый класс Человек со свойствами имя, возраст и пол. От этого класса унаследуйте классы Мужчина и Женщина и добавьте в них свойства, связанные с социальным положением (например, семейное положение,количество детей и т.д.)."
class Person:

    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self) -> str:
        return f"Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}"

    def __str__(self) -> str:
        return self.display_info()

class Man(Person):

    def __init__(self, name: str, age: int, marital_status: str = "не женат",
                 children_count: int = 0, occupation: str = "не указана"):
        super().__init__(name, age, "мужской")
        self.marital_status = marital_status
        self.children_count = children_count
        self.occupation = occupation

    def display_gender_info(self) -> str:
        return "Пол объекта: мужской"

    def display_social_info(self) -> str:
        return f"Семейное положение: {self.marital_status}, Детей: {self.children_count}, Профессия: {self.occupation}"

    def display_info(self) -> str:
        return f"{super().display_info()}, {self.display_social_info()}"

    def __str__(self) -> str:
        return self.display_info()

class Woman(Person):

    def __init__(self, name: str, age: int, marital_status: str = "не замужем",
                 children_count: int = 0, education: str = "не указано"):
        super().__init__(name, age, "женский")
        self.marital_status = marital_status
        self.children_count = children_count
        self.education = education  # Исправлено: теперь это обычный атрибут

    def display_gender_info(self) -> str:
        return "Пол объекта: женский"

    def display_social_info(self) -> str:
        return f"Семейное положение: {self.marital_status}, Детей: {self.children_count}, Образование: {self.education}"

    def display_info(self) -> str:
        return f"{super().display_info()}, {self.display_social_info()}"

    def __str__(self) -> str:
        return self.display_info()

print("ТЕСТИРОВАНИЕ КЛАССА Person")
person1 = Person("Алексей Петров", 30, "мужской")
print(person1)
print()

print("ТЕСТИРОВАНИЕ КЛАССА Man")
man1 = Man("Иван Сидоров", 35, "женат", 2, "Инженер")
print(man1)
print(man1.display_gender_info())

print("Изменение свойств мужчины ")
man1.marital_status = "разведён"
man1.children_count = 1
print(man1)
print()

print("ТЕСТИРОВАНИЕ КЛАССА Woman")
woman1 = Woman("Мария Иванова", 28, "замужем", 1, "Высшее")
print(woman1)
print(woman1.display_gender_info())

print("Изменение свойств женщины ")
woman1.education = "Магистратура"
woman1.children_count = 2
print(woman1)
print()

print("ПРОВЕРКА ПОЛИМОРФИЗМА")
people = [
    Person("Тестовый Человек", 25, "не указан"),
    Man("Дмитрий Козлов", 40, "женат", 3, "Врач"),
    Woman("Елена Смирнова", 32, "не замужем", 0, "Среднее специальное")
]

for i, p in enumerate(people, 1):
    print(f"{i}. {p}")
    if hasattr(p, "display_gender_info"):
        print(f"  {p.display_gender_info()}")

print("Все тесты завершены успешно!")
