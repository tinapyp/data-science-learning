import time
import os

db = {"task": [], "due": [], "priority": []}


def clear_screen():
    os.system("clear")


def add_task():
    clear_screen()
    print("ADD\n")
    task = input("What is it? ")
    due = input("When is it due? ")
    priority = input("How Important? ")
    return task, due, priority


def save_task(task, due, priority):
    db["task"].append(task)
    db["due"].append(due)
    db["priority"].append(priority)
    time.sleep(0.5)
    clear_screen()


def edit_task(input_edit):
    clear_screen()
    new_task = input("New Title: ")
    new_due = input("New Due Date: ")
    new_priority = input("New Priority: ")
    for i in range(len(db["task"])):
        if input_edit == db["task"][i]:
            db["task"][i] = new_task
            db["due"][i] = new_due
            db["priority"][i] = new_priority
    print("Successful Edit")
    time.sleep(0.5)
    clear_screen()


def remove_task(input_remove):
    for i in range(len(db["task"])):
        if input_remove == db["task"][i]:
            del db["task"][i]
            del db["due"][i]
            del db["priority"][i]
            break
    print("Task removed successfully.")
    time.sleep(0.5)
    clear_screen()


def view_all_tasks():
    for i in range(len(db["task"])):
        print(f"{db['task'][i]:^10} | {db['due'][i]:^10} | {db['priority'][i]:^10}")
    print()
    time.sleep(1)
    clear_screen()


def view_priority_tasks(input_priority):
    for i in range(len(db["task"])):
        if db["priority"][i] == input_priority:
            print(f"{db['task'][i]:^10} | {db['due'][i]:^10} | {db['priority'][i]:^10}")
    print()
    time.sleep(1)
    clear_screen()


while True:
    print("🌟 Life Organizer 🌟\n")
    print("Welcome to the life organizer.\n")
    menu = """
    1: Add
    2: View
    3: Remove
    4: Edit
    """
    print(menu)
    main_menu = int(input("Choose the Menu: "))

    if main_menu == 1:
        task, due, priority = add_task()
        save_task(task, due, priority)
        print("Added")

    elif main_menu == 2:
        clear_screen()
        print("View\n")
        view_menu = """
        1: View All
        2: View Priority
        """
        print(view_menu)
        view_menu_choice = int(input("Choose View Option: "))
        if view_menu_choice == 1:
            view_all_tasks()
        elif view_menu_choice == 2:
            input_priority = str(input("Which priority? "))
            view_priority_tasks(input_priority)

    elif main_menu == 3:
        clear_screen()
        print("Remove\n")
        input_remove = input("What task do you want to remove? ")
        remove_task(input_remove)
        view_all_tasks()

    elif main_menu == 4:
        input_edit = input("What do you want to edit? ")
        time.sleep(0.2)
        clear_screen()
        print("Edit\n")
        edit_task(input_edit)
        view_all_tasks()
