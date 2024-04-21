import os

DB_USERNAME = os.environ["USERNAME"]
DB_PASSWORD = os.environ["PASSWORD"]


def authentication(username, password):
    if username == DB_USERNAME and password == DB_PASSWORD:
        return True
    else:
        return False


def save_data(path, post="[]"):
    with open(path, "w") as f:
        f.write(post)


def read_data(path):
    with open(path, "r") as f:
        posts: list = list(eval(f.read()))
    return posts


def read_data_html(path):
    with open(path, "r") as f:
        posts: str = f.read()
    return posts
