import tkinter as tk
import os

root = tk.Tk()
root.title("Guess Who?!")


def show_image():
    try:
        name = entry.get()
        file_path = name + ".png"
        print(file_path)
        if os.path.exists(file_path):
            image = tk.PhotoImage(file=file_path)
            image = image.subsample(2)
            canvas.create_image(150, 150, image=image)
        else:
            raise FileNotFoundError("File not found")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, str(e))


entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Search", padx=20, pady=10, command=show_image)
button.pack()

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

root.mainloop()
