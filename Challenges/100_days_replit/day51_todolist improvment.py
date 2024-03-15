import os, time

task_list = []

if not os.path.exists("task.txt"):
    with open("task.txt", "w") as file:
        file.close()
else:
    with open("task.txt", "r") as file:
        task_list = eval(file.read())
        file.close()


def add(task):
    task_list.append(task)


def view():
    for idx in range(len(task_list)):
        print(f"{idx+1}. {task_list[idx]}")
    print()


def edit(editTask, newTask):
    if editTask in task_list:
        index = task_list.index(editTask)
        task_list[index] = newTask
    else:
        print("Task not found!")


def remove(task):
    if task in task_list:
        index = task_list.index(task)
        del task_list[index]
    else:
        print("Task not found!")


while True:
    print("To do List Manager:\n")

    menu = input(
        "Do you want to view, add, edit, or remove an item from the to do list? "
    )

    if menu == "add":
        _ = input("What do you want to do? \n")
        add(_)
        view()
        time.sleep(1)
        os.system("clear")

    elif menu == "edit":
        view()
        editTask = input("Enter the task you want to edit: ")
        newTask = input("Enter the new task: ")
        edit(editTask, newTask)
        view()
        time.sleep(0.5)
        os.system("clear")

    elif menu == "remove":
        view()
        _ = input("What do you want to remove? \n")
        alert = input("Are you sure you want to remove this? \n")
        if alert.lower() in ("yes", "y"):
            remove(_)
            print("Task successfull remove")
            time.sleep(0.5)
            os.system("clear")

    elif menu == "view":
        view()
        time.sleep(1)
        os.system("clear")

    with open("task.txt", "w") as file:
        file.write(str(task_list))
        file.close()
