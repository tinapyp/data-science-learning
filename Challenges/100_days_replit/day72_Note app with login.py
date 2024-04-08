from replit import db
import random
import os
import datetime


def get_info_account() -> str:
  username = input('Username > ')
  password = input('Password > ')
  return username, password


def hash_login(password: str, salt: str) -> str:
  hash_password = hash(password + salt)
  return hash_password


def add_user(username: str, password: str) -> None:
  try:
    salt = str(random.randint(1000, 10000))
    hash_password = hash_login(password=password, salt=salt)
    db[username] = {
      'db_username': username,
      'db_password': hash_password,
      'db_salt': salt
    }
    print("User added")
  except Exception as e:
    print('Error :', e)


def auth_challange(username: str, password: str) -> bool:
  salt = db[username]['db_salt']
  db_username = db[username]['db_username']
  db_password = db[username]['db_password']
  if username == db_username and hash_login(password, salt) == db_password:
    return True
  else:
    return False


def login(username: str, password: str) -> None:
  try:
    if auth_challange(username, password):
      return True
    else:
      print('Username and Password not Match!')
  except Exception as e:
    print('Error :', e)


def load_note():
  if 'note.txt' not in os.listdir():
    data = []
    with open('note.txt', 'w') as file:
      file.write(str(data))
      return data
  else:
    with open('note.txt', 'r') as file:
      data = eval(file.read())
      return data


def add_note():
  data = load_note()
  time = datetime.datetime.now()
  note = input('Note > ')
  data.append([time, note])
  print('Note saved')
  with open('note.txt', 'w') as file:
    file.write(str(data))
    return data


def view_note():
  data = load_note()
  for idx, data in enumerate(data):
    print(data[0], data[1])


def note_app():
  menu = input("""1: Add
2: View
""")
  if menu == '1':
    add_note()
  elif menu == '2':
    view_note()


def main():
  home = input("""1: Login
2: Register
> """)

  if home == '1':
    username, password = get_info_account()
    if login(username, password):
      while True:
        note_app()
  elif home == '2':
    username, password = get_info_account()
    add_user(username, password)


if __name__ == "__main__":
  main()