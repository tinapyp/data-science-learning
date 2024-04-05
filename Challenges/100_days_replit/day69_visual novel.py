import tkinter as tk


def story1() -> None:
    global button1
    global button2
    global image
    image = tk.PhotoImage(file="story1menu.png")
    image = image.subsample(3)
    canvas.itemconfig(container, image=image)
    button1.pack_forget()
    button2.pack_forget()
    button1 = tk.Button(text="Let's Use VSCode", command=happy_ending)
    button1.pack()
    button2 = tk.Button(text="Use VIM", command=bad_ending)
    button2.pack()


def story2() -> None:
    global button1
    global button2
    global image
    image = tk.PhotoImage(file="story2menu.png")
    image = image.subsample(3)
    canvas.itemconfig(container, image=image)
    button1.pack_forget()
    button2.pack_forget()
    button1 = tk.Button(text="Vim is Awesome", command=bad_ending)
    button1.pack()
    button2 = tk.Button(text="i make VIM config", command=bad_ending)
    button2.pack()


def happy_ending() -> None:
    global button1
    global button2
    global image
    image = tk.PhotoImage(file="love.png")
    image = image.subsample(3)
    canvas.itemconfig(container, image=image)
    button1.pack_forget()
    button2.pack_forget()
    button1 = tk.Button(text="Restart!", command=home)
    button1.pack()


def bad_ending() -> None:
    global button1
    global button2
    global image
    image = tk.PhotoImage(file="sad.png")
    image = image.subsample(3)
    canvas.itemconfig(container, image=image)
    button1.pack_forget()
    button2.pack_forget()
    button1 = tk.Button(text="Restart!", command=home)
    button1.pack()


def home() -> None:
    global button1
    global button2
    global image
    image = tk.PhotoImage(file="mainStory.png")
    image = image.subsample(3)
    canvas.itemconfig(container, image=image)
    button1.pack_forget()
    button2.pack_forget()
    button1 = tk.Button(text="What code editor u using?", command=story1)
    button1.pack()
    button2 = tk.Button(text="Just use VIM lol", command=story2)
    button2.pack()


root = tk.Tk()
root.title("Light Novel")
root.geometry("400x400")

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()
image = tk.PhotoImage(file="mainStory.png")
image = image.subsample(3)
container = canvas.create_image(150, 2, image=image)

button1 = tk.Button(text="What code editor u using?", command=story1)
button1.pack()
button2 = tk.Button(text="Just use VIM lol", command=story2)
button2.pack()

root.mainloop()
