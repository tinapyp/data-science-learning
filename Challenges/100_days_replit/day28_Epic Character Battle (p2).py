import random
import os
import time


def roll(number):
    return random.randint(1, number)


def calculate_health():
    return ((roll(6) * roll(12)) / 2) + 10


def calculate_strength():
    return ((roll(6) * roll(12)) / 2) + 12


def print_with_typing(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print()


def generate_character():
    legend = input("Name your Legend: ")
    char_type = input("Character Type (Human, Elf, Wizard, Orc): ")
    health_val = calculate_health()
    strength_val = calculate_strength()
    return legend, char_type, health_val, strength_val


def player_attack(p1_legend, p2_legend, p1_strength, p2_strength):
    while True:
        p1_cache = roll(6)
        p2_cache = roll(6)
        if p1_cache != p2_cache:
            break
    attacker = p1_legend if p1_cache > p2_cache else p2_legend
    damage = p1_strength if p1_cache > p2_cache else p2_strength
    return attacker, damage


def battle(p1_legend, p1_health, p1_strength, p2_legend, p2_health, p2_strength):
    while p1_health > 0 and p2_health > 0:
        attacker, damage = player_attack(p1_legend, p2_legend, p1_strength, p2_strength)
        print(f"{attacker} takes a hit, with {damage} damage")
        if attacker == p1_legend:
            p2_health -= damage
        else:
            p1_health -= damage
        print(p1_legend, " Health : ", p1_health)
        print(p2_legend, " Health : ", p2_health)
        print()
    return p1_legend if p1_health > 0 else p2_legend


print("⚔️ CHARACTER BUILDER ⚔️")
print()

while True:
    p1_legend, p1_char_type, p1_health, p1_strength = generate_character()
    print_with_typing(f"Generating stats for {p1_legend}...")
    time.sleep(0.5)

    print()
    print(f"Legend: {p1_legend}")
    print(f"HEALTH: {p1_health}")
    print(f"STRENGTH: {p1_strength}")
    print()
    print_with_typing("Who are they battling?")
    print()

    p2_legend, p2_char_type, p2_health, p2_strength = generate_character()

    print_with_typing(f"Generating stats for {p2_legend}...")
    time.sleep(0.5)

    print()
    print(f"Legend: {p2_legend}")
    print(f"HEALTH: {p2_health}")
    print(f"STRENGTH: {p1_strength}")
    print()

    time.sleep(1)
    os.system("clear")

    print("⚔️ BATTLE TIME ⚔️")
    print_with_typing("The battle begins!")
    print()

    os.system("clear")
    print("⚔️ BATTLE TIME ⚔️")
    print_with_typing("The battle begins!\n")
    winner = battle(
        p1_legend, p1_health, p1_strength, p2_legend, p2_health, p2_strength
    )
    print(f"The winner is: {winner}\n")
    print()

    answer = input("Play Again? (yes/no): ").lower()
    if answer == "no":
        print("Thank you for playing")
        break
    else:
        print("Let's play!")
        time.sleep(0.5)
        os.system("clear")
        continue
