"""Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых
положительных и отрицательных чисел. Сформировать новый текстовый файл
 (.txt) следующего вида, предварительно выполнив
 требуемую обработку элементов:"""
import random
def main():
    input_filename = 'data_var13_input.txt'
    output_filename = 'data_var13_output.txt'

    count_elements = 20
    min_val = -50
    max_val = 50

    numbers = [random.randint(min_val, max_val) for _ in range(count_elements)]
    try:
        with open(input_filename, 'w', encoding='utf-8') as f_in:
            f_in.write(' '.join(map(str, numbers)))
        print(f"[+] Входной файл '{input_filename}' создан с {count_elements} элементами.")
    except IOError as e:
        print(f"[-] Ошибка записи входного файла: {e}")
        return

    try:
        with open(input_filename, 'r', encoding='utf-8') as f_in:
            content = f_in.read().strip()

        if not content:
            print("[-] Входной файл пуст.")
            return

        data_list = [int(x) for x in content.split()]
    except (IOError, ValueError) as e:
        print(f"[-] Ошибка чтения или преобразования: {e}")
        return

    n = len(data_list)

    max_value = max(data_list)
    max_index_zero_based = data_list.index(max_value)
    max_index_one_based = max_index_zero_based + 1

    third_part = n // 3
    start_idx = third_part
    end_idx = n - third_part

    middle_third = data_list[start_idx:end_idx]

    if middle_third:
        product = 1
        for num in middle_third:
            product *= num
        product_str = str(product)
    else:
        product_str = "Недостаточно элементов"

    try:
        with open(output_filename, 'w', encoding='utf-8') as f_out:
            f_out.write(f"Исходные данные: {' '.join(map(str, data_list))}\n")
            f_out.write(f"Количество элементов: {n}\n")

            f_out.write(f"Индекс первого максимального элемента: {max_index_one_based}\n")
            f_out.write(f"Произведение элементов средней трети: {product_str}\n")

        print(f"[+] Результаты успешно записаны в '{output_filename}'.")
        print(f"    Максимальный элемент: {max_value} (индекс {max_index_one_based})")
        print(f"    Средняя треть ({start_idx}:{end_idx}): {middle_third}")
        print(f"    Произведение средней трети: {product_str}")

    except IOError as e:
        print(f"[-] Ошибка записи выходного файла: {e}")

if __name__ == "__main__":
    main()