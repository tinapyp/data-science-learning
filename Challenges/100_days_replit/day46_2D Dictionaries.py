moka_deck = {}


def menu_check():
    menu = input("Continue? y/n > ").lower().strip()[0]
    if menu != "y":
        exit()


def get_data():
    name = input("Input the beast name > ")
    element = input("Input the beast element > ")
    move = input("Input the beast special move > ")
    hp = input("Input the beast starting HP > ")
    mp = input("Input the beast starting MP > ")
    return name, element, move, hp, mp


def store_data(db, name, element, move, hp, mp):
    id = "moke" + len(db) + 1
    db[id] = {"name": name, "element": element, "move": move, "hp": hp, "mp": mp}


def display(db):
    print("\nMokeBeast Deck:")
    print("{:^15} | {:^20} | {:^10} | {:^10}".format("Name", "Element", "HP", "MP"))
    for index, data in db.items():
        print(
            "{:^15} | {:^20} | {:^10} | {:^10}".format(
                data["name"], data["element"], data["hp"], data["mp"]
            )
        )


print("🌟MokeBeast Generator🌟\n")

while True:
    name, element, move, hp, mp = get_data()
    store_data(moka_deck, name, element, move, hp, mp)
    display(moka_deck)
    menu_check()
