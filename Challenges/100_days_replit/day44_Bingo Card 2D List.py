import random

print("Grandma Bingo Card Generator\n")


def get_random_number():
    number = random.randint(0, 91)
    return number


def bingo_card():
    bingo_card = []
    for row in range(3):
        row_val = []
        for col in range(3):
            number = get_random_number()
            row_val.append(number)
        bingo_card.append(row_val)
    bingo_card[1][1] = "BINGO"
    return bingo_card


def pretty_print(card):
    for row in card:
        for col in row:
            print(f"{col:^10}", end=" | ")
        print()


def number_choosed(val, card):
    for i, row in enumerate(card):
        for idx, col in enumerate(row):
            if val == col:
                card[i][idx] = "X"
    return card


def is_winning(card):
    counter = 0
    for i, row in enumerate(card):
        for idx, col in enumerate(row):
            if col == "X":
                counter += 1
    if counter == 8:
        return True
    else:
        return False


bingo_card = bingo_card()
while True:
    pretty_print(bingo_card)
    number = int(input("Choose your number: "))
    bingo_card = number_choosed(number, bingo_card)
    if is_winning(bingo_card):
        print("Bingo! You have won!")
        break
    else:
        print()
