import os
import random

tasks = []

if "tasks.txt" not in os.listdir():
    with open("tasks.txt", "w") as file:
        file.write(str(tasks))
        file.close()
else:
    with open("tasks.txt", "r") as file:
        tasks = eval(file.read())
        file.close()


def add(task, tasks):
    tasks.append(task)
    print("new task added")
    print()


def view():
    for idx, task in enumerate(tasks):
        print(f"{idx+1}. {task}")
    print()


def edit(task, new_task, tasks):
    if task in tasks:
        idx = task.index(task)
        tasks[idx] = new_task
        print(f"{task} updated")
    else:
        print(f"{task} not found")
    print()


def remove(task, tasks):
    if task in tasks:
        tasks.remove(task)
        print(f"{task} removed from database")
    else:
        print(f"{task} not found")
    print()


def backup(tasks):
    if "hello" not in os.listdir():
        os.mkdir("hello/")
    file = open(f"hello/tasks-{random.randint(1,1000)}.txt", "w")
    file.write(str(tasks))
    file.close()


while True:
    menu = input(
        """1: Add
2: View
3: Edit
4: Remove
> """
    )
    print()

    if menu == "1":
        task = input("New Task > ")
        add(task, tasks)

    elif menu == "2":
        view()

    elif menu == "3":
        task = input("Task want to edit > ")
        new_task = input("New Task > ")
        edit(task, new_task, tasks)

    elif menu == "4":
        task = "Task want to remove > "
        remove(task, tasks)

    backup(tasks)
    with open("tasks.txt", "w") as file:
        file.write(str(tasks))
        file.close()
