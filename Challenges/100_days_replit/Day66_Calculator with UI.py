import tkinter as tk


def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))


def button_clear():
    entry.delete(0, tk.END)


def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ("1", 1, 0),
    ("2", 1, 1),
    ("3", 1, 2),
    ("/", 1, 3),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),
    ("7", 3, 0),
    ("8", 3, 1),
    ("9", 3, 2),
    ("+", 3, 3),
    ("C", 4, 0),
    ("0", 4, 1),
    ("=", 4, 2),
    ("-", 4, 3),
]

for button_text, row, col in buttons:
    if button_text == "=":
        button = tk.Button(
            root, text=button_text, padx=20, pady=10, command=button_equal
        )

    elif button_text == "C":
        button = tk.Button(
            root, text=button_text, padx=20, pady=10, command=button_clear
        )

    else:
        button = tk.Button(
            root,
            text=button_text,
            padx=20,
            pady=10,
            command=lambda text=button_text: button_click(text),
        )
    button.grid(row=row, column=col)

root.mainloop()
