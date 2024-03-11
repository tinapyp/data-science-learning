import random

print("Grandma Bingo Card\n\n")


def get_random():
    return random.randint(1, 90)


def bingo_card():
    bingo_card = []

    for row in range(3):
        bingo_row = []
        for col in range(3):
            bingo_row.append(get_random())
        bingo_card.append(bingo_row)

    bingo_card[1][1] = "BINGO"
    return bingo_card


bingo_card = bingo_card()
for row in bingo_card:
    row_str = ""
    for val in row:
        row_str += str(val) + " | "
    print(row_str[:-2].center(50))
    print("-----------------".center(50))
