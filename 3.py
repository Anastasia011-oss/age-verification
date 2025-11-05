import tkinter as tk

root = tk.Tk()
root.title("Калькулятор")
root.geometry("400x400")
root.configure(bg="#f2f2f2")

label1 = tk.Label(root, text="Введите первое число:", font=("Arial", 12), bg="#f2f2f2")
label1.pack(pady=(20, 5))
entry1 = tk.Entry(root, font=("Arial", 12), width=20, justify="center")
entry1.pack(pady=5)

label2 = tk.Label(root, text="Введите второе число:", font=("Arial", 12), bg="#f2f2f2")
label2.pack(pady=(10, 5))
entry2 = tk.Entry(root, font=("Arial", 12), width=20, justify="center")
entry2.pack(pady=5)

label_res = tk.Label(root, text="", font=("Arial", 18, "bold"), fg="blue", bg="#f2f2f2")
label_res.pack(pady=20)

def calculate(operation):
    try:
        a = float(entry1.get())
        b = float(entry2.get())

        if operation == '+':
            result = a + b
        elif operation == '-':
            result = a - b
        elif operation == '*':
            result = a * b
        elif operation == '/':
            if b == 0:
                label_res.configure(text="Деление на 0!", fg="red")
                return
            result = a / b

        label_res.configure(text=f"Результат: {result}", fg="green")

    except ValueError:
        label_res.configure(text="Введите числа!", fg="orange")

def clear_fields():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    label_res.configure(text="", fg="blue")

frame = tk.Frame(root, bg="#f2f2f2")
frame.pack(pady=10)

btn_add = tk.Button(frame, text="+", font=("Arial", 14), width=4, command=lambda: calculate('+'))
btn_add.grid(row=0, column=0, padx=5)

btn_sub = tk.Button(frame, text="-", font=("Arial", 14), width=4, command=lambda: calculate('-'))
btn_sub.grid(row=0, column=1, padx=5)

btn_mul = tk.Button(frame, text="*", font=("Arial", 14), width=4, command=lambda: calculate('*'))
btn_mul.grid(row=0, column=2, padx=5)

btn_div = tk.Button(frame, text="/", font=("Arial", 14), width=4, command=lambda: calculate('/'))
btn_div.grid(row=0, column=3, padx=5)

btn_clear = tk.Button(root, text="Очистить", font=("Arial", 14), bg="#dddddd", command=clear_fields)
btn_clear.pack(pady=15)

root.mainloop()
