"Задание 1. В соответствии с номером варианта перейти по ссылке на прототип. Реализовать его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально приближенный к оригиналу (см. таблицу 1)."
import tkinter as tk
from tkinter import ttk

def on_click_prev(event):
    print("Нажата кнопка 'Назад' (Step 1)")

def on_click_next(event):
    print("Нажата кнопка 'Далее' (Step 3)")

def on_enter(event, item_id):
    canvas.itemconfig(item_id, fill="#9fd47a")

def on_leave(event, item_id):
    canvas.itemconfig(item_id, fill="#81c14f")

root = tk.Tk()
root.title("Educational Details")
root.geometry("580x600")

bg_color = "#3f6e9a"
entry_bg = "#ffffff"
btn_color = "#81c14f"

root.configure(bg=bg_color)

label_font = ("Segoe UI", 11, "normal")
entry_font = ("Segoe UI", 10, "normal")

main_frame = tk.LabelFrame(
    root,
    text="Educational Details",
    font=("Segoe UI", 14, "bold"),
    bg=bg_color,
    fg="white",
    borderwidth=1,
    relief="solid",
    highlightbackground="white"
)
main_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)

tk.Label(main_frame, text="University :", bg=bg_color, fg="white", font=label_font, width=15, anchor='e').grid(row=0, column=0, pady=8, padx=5, sticky='e')
tk.Entry(main_frame, width=30, bg=entry_bg, bd=0, font=entry_font, highlightthickness=1).grid(row=0, column=1, pady=8, padx=5, sticky='w')

tk.Label(main_frame, text="Institute :", bg=bg_color, fg="white", font=label_font, width=15, anchor='e').grid(row=1, column=0, pady=8, padx=5, sticky='e')
tk.Entry(main_frame, width=30, bg=entry_bg, bd=0, font=entry_font, highlightthickness=1).grid(row=1, column=1, pady=8, padx=5, sticky='w')

tk.Label(main_frame, text="Branch :", bg=bg_color, fg="white", font=label_font, width=15, anchor='e').grid(row=2, column=0, pady=8, padx=5, sticky='e')
branch_combo = ttk.Combobox(main_frame, values=["-- select --", "CS", "IT", "Mech"], state="readonly", width=27, font=entry_font)
branch_combo.set("-- select --")
branch_combo.grid(row=2, column=1, pady=8, padx=5, sticky='w')

degree_frame = tk.Frame(main_frame, bg=bg_color)
degree_frame.grid(row=3, column=1, sticky='w')

tk.Label(main_frame, text="Degree :", bg=bg_color, fg="white", font=label_font, width=15, anchor='e').grid(row=3, column=0, pady=8, padx=5, sticky='e')

degree_combo = ttk.Combobox(degree_frame, values=["-- select --", "Bachelor", "Master"], state="readonly", width=12, font=entry_font)
degree_combo.set("-- select --")
degree_combo.pack(side=tk.LEFT, padx=(0, 15))

degree_var = tk.StringVar()

tk.Radiobutton(degree_frame, text="Pursuing", variable=degree_var, value="Pursuing",
               background=bg_color, foreground="white", selectcolor=bg_color,
               activebackground=bg_color, activeforeground="white").pack(side=tk.LEFT)
tk.Radiobutton(degree_frame, text="Completed", variable=degree_var, value="Completed",
               background=bg_color, foreground="white", selectcolor=bg_color,
               activebackground=bg_color, activeforeground="white").pack(side=tk.LEFT)

tk.Label(main_frame, text="Average CPI :", bg=bg_color, fg="white", font=label_font, width=15, anchor='e').grid(row=4, column=0, pady=8, padx=5, sticky='e')

cpi_frame = tk.Frame(main_frame, bg=bg_color)
cpi_frame.grid(row=4, column=1, sticky='w')

ttk.Spinbox(cpi_frame, from_=0, to=10, width=5, font=entry_font).pack(side=tk.LEFT)
tk.Label(cpi_frame, text="Upto", bg=bg_color, fg="white", font=label_font).pack(side=tk.LEFT, padx=5)
ttk.Spinbox(cpi_frame, from_=1, to=8, width=3, font=entry_font).pack(side=tk.LEFT)
tk.Label(cpi_frame, text="Th Semester", bg=bg_color, fg="white", font=label_font).pack(side=tk.LEFT)

tk.Label(main_frame, text="Experience :", bg=bg_color, fg="white", font=label_font, width=15, anchor='e').grid(row=5, column=0, pady=8, padx=5, sticky='e')
exp_frame = tk.Frame(main_frame, bg=bg_color)
exp_frame.grid(row=5, column=1, sticky='w')
ttk.Spinbox(exp_frame, from_=0, to=50, width=5, font=entry_font).pack(side=tk.LEFT)
tk.Label(exp_frame, text="Years", bg=bg_color, fg="white", font=label_font).pack(side=tk.LEFT)

tk.Label(main_frame, text="Your Website Or Blog :", bg=bg_color, fg="white", font=label_font, width=15, anchor='e').grid(row=6, column=0, pady=8, padx=5, sticky='e')
tk.Entry(main_frame, width=30, bg=entry_bg, bd=0, font=entry_font, textvariable=tk.StringVar(value="http://"), highlightthickness=1).grid(row=6, column=1, pady=8, padx=5, sticky='w')

nav_frame = tk.Frame(root, bg=bg_color)
nav_frame.pack(pady=25)

canvas = tk.Canvas(nav_frame, width=160, height=50, bg=bg_color, highlightthickness=0)
canvas.pack()

btn_left = canvas.create_oval(5, 5, 45, 45, fill=btn_color, outline="")

canvas.create_polygon(30, 15, 30, 35, 15, 25, fill="white", outline="")

canvas.create_text(80, 25, text="Step 2", fill="white", font=("Segoe UI", 11, "bold"))

btn_right = canvas.create_oval(115, 5, 155, 45, fill=btn_color, outline="")

canvas.create_polygon(130, 15, 130, 35, 145, 25, fill="white", outline="")

canvas.tag_bind(btn_left, "<Button-1>", on_click_prev)
canvas.tag_bind(btn_left, "<Enter>", lambda e: on_enter(e, btn_left))
canvas.tag_bind(btn_left, "<Leave>", lambda e: on_leave(e, btn_left))
canvas.tag_bind(btn_left, "<Enter>", lambda e: canvas.config(cursor="hand2"))
canvas.tag_bind(btn_left, "<Leave>", lambda e: canvas.config(cursor=""))

canvas.tag_bind(btn_right, "<Button-1>", on_click_next)
canvas.tag_bind(btn_right, "<Enter>", lambda e: on_enter(e, btn_right))
canvas.tag_bind(btn_right, "<Leave>", lambda e: on_leave(e, btn_right))
canvas.tag_bind(btn_right, "<Enter>", lambda e: canvas.config(cursor="hand2"))
canvas.tag_bind(btn_right, "<Leave>", lambda e: canvas.config(cursor=""))

root.mainloop()