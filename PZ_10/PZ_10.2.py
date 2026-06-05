"""Из предложенного текстового файла (text18-13.txt) вывести на экран его содержимое,
 количество символов в тексте. Сформировать новый файл, в который поместить текст в стихотворной
  форме предварительно вставив после строки N (N – задается пользователем)
 произвольную фразу."""
with open('text18-13.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
content = ''.join(lines)
print("Содержимое файла:")
print(content)

char_count = 0
for char in content:
    char_count += 1
print(f"Количество символов в тексте: {char_count}")
n_line = int(input("Введите номер строки N, после которой нужно вставить фразу: "))
user_phrase = input("Введите произвольную фразу: ")

if n_line < 1:
    n_line = 1
elif n_line > len(lines):
    n_line = len(lines)

lines.insert(n_line, user_phrase + '\n')
modified_content = ''.join(lines)

with open('text18-13_modified.txt', 'w', encoding='utf-8') as f:
    f.write(modified_content)
print("Новый файл создан: text18-13_modified.txt")