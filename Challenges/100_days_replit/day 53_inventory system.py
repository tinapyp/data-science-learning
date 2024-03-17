import os

items = []

if not os.path.exists('items.txt'):
  with open('items.txt', 'w') as file:
    file.close()
else:
  with open('items.txt', 'r') as file:
    items = eval(file.read())
    file.close()


def input_data():
  item = input('Item to add > ')
  return item


def save_item(item, db):
  db.append(item)
  print('Item successfull added')


def view():
  for item in list(set(items)):
    print(f"{item} - {items.count(item)}")
  print()


while True:
  print('INVENTORY/n==============/n')
  menu = input("""1. Add
2. Remove
3. View
> """)

  if menu == '1':
    item = input_data()
    save_item(item, items)
  elif menu == '2':
    remove_item = input('what do you want to remove?')
    if remove_item in items:
      items.remove(remove_item)
  elif menu == '3':
    view()

  with open('items.txt', 'w') as file:
    file.write(str(items))
    file.close()
