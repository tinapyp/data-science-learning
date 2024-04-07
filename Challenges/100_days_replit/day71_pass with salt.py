from replit import db
import random


def hash_password(password: str) -> str:
    salt = str(random.randint(1000, 10000))
    password = f"{password}{salt}"
    password = hash(password)
    return password, salt


def add_user(username: str, password: str) -> None:
    try:
        password, salt = hash_password(password)
        db[username] = {"password": password, "salt": salt}
        print("User Added")
    except Exception as e:
        print(f"Error: {e}")


def check_password(password: str) -> bool:
    try:
        salt = db[username]["salt"]
        hash_password = db[username]["password"]
        password = f"{password}{salt}"
        if hash(password) == hash_password:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")


def login(username: str, password: str) -> None:
    if check_password(password):
        print("Login Successfull")
    else:
        print("Username and Password not match!")


while True:
    menu = input(
        """
1: New User
2: Login
3: Exit
> """
    )
    if menu == "1":
        username = str(input("Username > "))
        password = str(input("Password > "))
        add_user(username=username, password=password)

    elif menu == "2":
        username = str(input("Username > "))
        password = str(input("Password > "))
        login(username=username, password=password)

    elif menu == "3":
        print("Thanks!")
        exit()
