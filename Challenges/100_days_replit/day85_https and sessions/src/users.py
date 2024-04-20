class User:
    def __init__(self, name: str, username: str, password: str):
        self.credentials = {"name": name, "username": username, "password": password}


class Users:
    def __init__(self):
        self.__users = {}

    def add_user(self, user):
        self.__users[user.credentials["username"]] = user.credentials

    def get_credentials(self, username):
        user_credentials = self.__users.get(username)
        if user_credentials:
            return user_credentials["username"], user_credentials["password"]
        else:
            return None, None

    def display_users(self):
        return self.__users.copy()

    def auth_login(self, inputted_username, inputted_password):
        db_username, db_password = self.get_credentials(inputted_username)
        if inputted_username == db_username and inputted_password == db_password:
            return True
        else:
            return False
