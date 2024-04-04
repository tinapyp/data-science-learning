import tkinter as tk
import os

root = tk.Tk()
root.title("Guess Who?!")


def show_image():
    global image
    name = entry.get()
    file_path = name + ".png"
    if os.path.exists(file_path):
        image = tk.PhotoImage(file=file_path)
        image = image.subsample(5)
        canvas.itemconfig(container, image=image)
    else:
        raise FileNotFoundError("File not found")


entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Search", padx=20, pady=10, command=show_image)
button.pack()

image = None
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()
container = canvas.create_image(150, 2, image=image)

root.mainloop()
