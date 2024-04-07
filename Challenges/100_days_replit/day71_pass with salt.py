from replit import db
import random


def hash_password(password: str, salt: str) -> int:
    hash_password = f"{password}{salt}"
    hash_password = hash(password)
    return hash_password


def add_user(username: str, password: str) -> None:
    try:
        salt = str(random.randint(1000, 10000))
        hash_password = hash_password(password, salt)
        db[username] = {"hash_password": hash_password, "salt": salt}
        print("User Added")
    except Exception as e:
        print(f"Error: {e}")


def check_password(password: str) -> bool:
    try:
        salt = db[username]["salt"]
        hash_password = db[username]["hash_password"]
        if hash(password, salt) == hash_password:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False


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
