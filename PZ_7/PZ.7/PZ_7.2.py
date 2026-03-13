#Дана строка-предложение на русском языке. Вывести самое длинное слово в предложении.
# Если таких слов несколько, то вывести первое из них. Словом считать набор символов, не содержащий пробелов, знаков препинания и ограниченный пробелами, знаками препинания или началом/концом строки
def samoe_dlinnoe_slovo(predlogenie):
    znaki = ".,!?;:-()\"'"
    for znak in znaki:
        predlogenie = predlogenie.replace(znak, ' ')
    slova = predlogenie.split()

    if slova:
        return max(slova, key=len)
    else:
        return None
try:
    text = input("Введите предложение: ")

    rezult = samoe_dlinnoe_slovo(text)
    if rezult:
        print(f"Самое длинное слово: '{rezult}'")
    else:
        print("В предложении нет слов")
except:
    print("Не удалось обработать ввод")