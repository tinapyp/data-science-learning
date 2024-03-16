import os

pizzaPrice = 50000
pizzaDB = []


def get_data():
  name = input("What is your name? ")
  topping = input("Toppings (separated by commas): ")
  size = input("Size (s, m, l)? ")
  quantity = int(input("How many pizzas? "))
  total = pizzaPrice * quantity
  order = [name, topping, size, quantity, total]
  pizzaDB.append(order)


def view_order():
  print("name", "topping", "size", "quantity", "total")
  for pizza in pizzaDB:
    name, topping, size, quantity, total = pizza
    print(name, topping, size, quantity, total)


try:
  if not os.path.exists("pizza.txt"):
    with open("pizza.txt", "w") as file:
      file.close()
  else:
    with open("pizza.txt", "r") as file:
      pizzaDB = eval(file.read())
      file.close()

  while True:
    menu = int(input("""Pizza Menu:
1: Add Pizza
2: View Pizza
> """))
    if menu == 1:
      get_data()
      print("Order Accepted")
    elif menu == 2:
      view_order()

    with open("pizza.txt", "w") as file:
      file.write(str(pizzaDB))
      file.close()
except Exception as e:
  print("Error: ", e)
