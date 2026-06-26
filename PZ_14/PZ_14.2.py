"Разработать программу с применением пакета tk, взяв в качестве условия одну любую задачу из ПЗ №№ 1 – 9."
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Практическое занятие №14 | Задание 2")
root.geometry("380x290")
root.resizable(False, False)

tk.Label(root, text="Проверка логического высказывания", font=("Arial", 13, "bold")).pack(pady=10)

frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=5)

tk.Label(frame_inputs, text="Число A:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_a = tk.Entry(frame_inputs, width=15)
entry_a.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Число B:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_b = tk.Entry(frame_inputs, width=15)
entry_b.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Число C:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_c = tk.Entry(frame_inputs, width=15)
entry_c.grid(row=2, column=1, padx=5, pady=5)

lbl_result = tk.Label(root, text="", font=("Arial", 12), wraplength=340)
lbl_result.pack(pady=10)

def check_statement():
    try:
        nums = [int(entry_a.get()), int(entry_b.get()), int(entry_c.get())]

        is_true = any(num > 0 for num in nums)

        result_text = "Истинно" if is_true else "Ложно"
        color = "green" if is_true else "red"

        lbl_result.config(
            text=f"«Хотя бы одно из чисел положительное» → {result_text}",
            fg=color
        )
    except ValueError:

        lbl_result.config(text="Ошибка: введите целые числа!", fg="red")
        messagebox.showwarning("Ошибка ввода", "Все поля должны содержать только целые числа.")

btn_check = tk.Button(
    root,
    text="Проверить условие",
    font=("Arial", 11),
    bg="#2196F3",
    fg="white",
    command=check_statement
)
btn_check.pack(pady=5)

root.mainloop()