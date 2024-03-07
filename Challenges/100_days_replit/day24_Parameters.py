import random

print("Infinity Dice 🎲")
print()


def get_input():
    while True:
        input_str = input("How many sides? ")
        if input_str.isdigit() and int(input_str) > 1:
            return int(input_str)
        else:
            print("Input correct number, and make sure it > 1")


def roll_dice(sides):
    return random.randint(1, sides)


def play_game():
    sides = get_input()

    while True:
        print("You Rolled:", roll_dice(sides))
        print()

        choice = input("Roll again? (Y/n): ").lower()
        if choice == "n":
            print("Thanks for playing!")
            break
        elif choice != "y":
            print("Invalid choice. Exiting...")
            break


play_game()
