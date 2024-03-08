import random
import os
import time


def roll(number):
    return random.randint(1, number)


def health():
    return ((roll(6) * roll(12)) / 2) + 10


def strength():
    return ((roll(6) * roll(12)) / 2) + 12


def print_with_typing(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print()


os.system("clear")

print_with_typing("⚔️ CHARACTER BUILDER ⚔️")
print()

while True:
    legend = input("Name your Legend: ")
    char_type = input("Character Type (Human, Elf, Wizard, Orc): ")
    print()

    print_with_typing(f"Generating stats for {legend}...")
    time.sleep(1)

    os.system("clear")

    print(f"Legend: {legend}")
    print(f"HEALTH: {health()}")
    print(f"STRENGTH: {strength()}")
    print()
    print_with_typing("May your name go down in Legend...")
    print()

    answer = input("Play Again? (yes/no): ").lower()
    if answer == "no":
        break
    else:
        os.system("clear")
        continue
