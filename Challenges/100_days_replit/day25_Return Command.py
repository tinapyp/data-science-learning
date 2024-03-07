import random

print("⚔️ CHARACTER STAT GENERATOR ⚔️")
print()


def health():
    a = random.randint(1, 6)
    b = random.randint(1, 8)
    c = a * b
    return c


while True:
    character = input("Name your warrior: ")
    warrior_health = health()
    print("Their health is {} hp".format(warrior_health))
    print()
    _ = input("Wanna create Other? (y/N)").lower()
    if _ == "y":
        continue
    else:
        print("Go play the game Warrior!")
        exit()
