import tkinter as tk

def add():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 + num2
    label_result.config(text="Результат: " + str(result))

def subtract():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 - num2
    label_result.config(text="Результат: " + str(result))

def multiply():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 * num2
    label_result.config(text="Результат: " + str(result))

def division():
    # Не рабочая функция
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 * num2
    label_result.config(text="Эта функция не работает")


root = tk.Tk()
root.title("Калькулятор")

label1 = tk.Label(root, text="Введите первое число:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Введите второе число:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

button_add = tk.Button(root, text="Сложение", command=add)
button_add.pack()

button_subtract = tk.Button(root, text="Вычитание", command=subtract)
button_subtract.pack()

button_multiply = tk.Button(root, text="Умножение", command=multiply)
button_multiply.pack()

button_division = tk.Button(root, text="Деление", command=division)
button_division.pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
