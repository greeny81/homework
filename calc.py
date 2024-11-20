import tkinter as tk

def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2
def insert_values(val):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, val)

def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)

def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)

def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)

window = tk.Tk() # создание окна
window.title("CALCUL")
window.geometry("300x210")
window.resizable(False, False)

button_add = tk.Button(window, text="+", width=2, height=1,font='Times 30', command=add )
button_add.place(x=10, y=70)
button_sub = tk.Button(window, text="-", width=2, height=1,font='Times 30', command=sub )
button_sub.place(x=80, y=70)
button_mul = tk.Button(window, text="*", width=2, height=1,font='Times 30', command=mul )
button_mul.place(x=150, y=70)
button_div = tk.Button(window, text="/", width=2, height=1,font='Times 30', command=div )
button_div.place(x=220, y=70)

number1_entry = tk.Entry(window, width=30)
number1_entry.place(x=90, y = 10 )
number2_entry = tk.Entry(window, width=30)
number2_entry.place(x=90, y = 40 )
answer_entry = tk.Entry(window, width=30)
answer_entry.place(x=50, y = 180 )

number1 = tk.Label(window, text="First num:")
number1.place(x=10, y=10)
number2 = tk.Label(window, text="Second num:")
number2.place(x=10, y=40)
number3 = tk.Label(window, text="Answer:")
number3.place(x=120, y=155)
window.mainloop()   # обновление событий окна
