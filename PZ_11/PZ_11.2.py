"""2 Составить список, в который будут включены только согласные буквы и привести
их к верхнему регистру. Список: ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели','Каир']."""
cities = ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']
letters = frozenset('бвгджзйклмнпрстфхцчшщ')

def gen_consonants(it):
    for word in it:
        for ch in word:
            if ch.lower() in letters:
                yield ch.upper()

print("Исходный список:", cities)
result = [c for c in gen_consonants(iter(cities))]
print("Результирующий список:", result)