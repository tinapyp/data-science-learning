import random, time, os

villains = {
    "Darth Vader": {
        "Intelligence": 95,
        "Evilness": 90,
        "Combat Skills": 85,
        "Force Mastery": 100,
    },
    "The Joker": {
        "Intelligence": 95,
        "Evilness": 100,
        "Combat Skills": 80,
        "Force Mastery": 100,
    },
}

stat = {1: "Intelligence", 2: "Evilness", 3: "Combat Skills", 4: "Force Mastery"}


def display_stat(villain, choose: int):
    key = stat.get(choose)
    return f"{villain} - {key} - {villains[villain][key]}"


def winning(p1, p2, choose: int):
    key = stat.get(choose)
    if villains[p1][key] > villains[p2][key]:
        print("Player Win")
    elif villains[p1][key] == villains[p2][key]:
        print("Draw")
    else:
        print("Computer Win")


print("Villains Data\n--------------\n")

print("Characters")
for key, val in villains.items():
    print(key)

while True:
    print("Choose a villain:")
    for i, villain in enumerate(villains.keys(), start=1):
        print(f"{i}. {villain}")

    choice = int(input("Enter your number villain of choice (ex:1)"))
    print()

    if choice in range(len(villains.keys())):
        choice = int(choice) - 1
        player_villain = list(villains.keys())[choice]
        print(player_villain, " has chosed by player")
        computer_villain = random.choice(list(villains.keys()))
        print(computer_villain, " has chosed by computer")
    else:
        print("Invalid choice. Please choose 1 or 2.")

    choice_stat = int(
        input(
            """
Choose your stat: 
1 - Intelligence
2 - Evilness
3 - Combat Skills
4 - Force Mastery
> """
        )
    )

    print()
    player_stat = display_stat(player_villain, choice_stat)
    print(player_stat)
    computer_stat = display_stat(computer_villain, choice_stat)
    print(computer_stat)
    print()

    winning(player_villain, computer_villain, choice_stat)
    print()
    time.sleep(1)
    os.system("clear")
