class Item:
    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price


class Store:
    def __init__(self) -> None:
        self.__cart = []

    def add_to_cart(self, item):
        self.__cart.append(item)

    def remove_from_cart(self, idx):
        self.__cart.pop(idx)

    def calculate_total(self):
        total = 0
        for item in self.__cart:
            total += item.price
        return total

    def display_item(self):
        for i in range(len(self.__cart)):
            print(i, " ", self.__cart[i].name)


def price_safety(price):
    if price <= 0:
        raise ValueError


store = Store()
# store.add_to_cart(Item("Fathin", 1000))
# store.add_to_cart(item=Item("Bob", 500))
# store.display_item()

print("Hello welcome to our store")
while True:
    store.display_item()
    store.calculate_total()

    print("Press a to add item")
    print("Press r to add item")
    print("Press x to add item")
    userInput: str = str(input("Please enter a command > "))
    if userInput.lower() == "x":
        break

    elif userInput.lower() == "a":
        try:
            name: str = str(input("what is name of product? > "))
            price: int = int(input("how much price of item? > "))
            price_safety(price)
            store.add_to_cart(item=Item(name, price))
        except ValueError:
            print("Please enter a valid input!")
            pass
        except Exception as e:
            print("Something Wrong, ", e)

    elif userInput.lower() == "r":
        try:
            idx: int = int(input("Please provided the index of the item to remove > "))
            store.remove_from_cart(idx)
        except ValueError:
            print("Please enter a valid input!")
            pass
        except Exception as e:
            print("Something Wrong, ", e)

    else:
        print("Please enter a valid input!")
