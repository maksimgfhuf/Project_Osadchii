#Организовать словарь 10 русско-английских слов, обеспечивающий "перевод" русского слова на английского.
perevod = {
    'привет': 'hello',
    'мир': 'world',
    'дом': 'house',
    'кот': 'cat',
    'собака': 'dog',
    'книга': 'book',
    'вода': 'water',
    'солнце': 'sun',
    'друг': 'friend',
    'работа': 'work'
}
russkoe_slovo = input("Введите слово для перевода: ").lower()
if russkoe_slovo in perevod:
    print(f"{russkoe_slovo} -> {perevod[russkoe_slovo]}")
else:
    print(f"Слово '{russkoe_slovo}' не найдено в словаре")

