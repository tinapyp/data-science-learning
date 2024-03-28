import datetime as dt
from replit import db


def login():
    username = input("Username : ")
    password = input("Password : ")
    if username == "admin" and password == "admin":
        pass
    else:
        print("Username or Password Wrong!")
        exit()


def add_note(input_note):
    now = dt.datetime.now()
    db[now] = input_note
    print("New note added")


def view_note():
    keys = list(db.keys())
    idx = len(keys) - 1
    while True:
        print(keys[idx], "->", db[keys[idx]])
        menu = input("Next or Exit? ")
        if menu.lower() == "exit":
            break
        idx -= 1


def main():
    while True:
        login()
        menu = input(
            """Note Taking
1. Add
2. View
> """
        )

        if menu == "1":
            input_note = str(input("New Note: "))
            add_note(input_note)
        elif menu == "2":
            view_note()
        elif menu == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid input. Please enter a valid option.")


if __name__ == "__main__":
    main()
