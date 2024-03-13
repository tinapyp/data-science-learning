print("🌟HIGH SCORE TABLE🌟")


def get_data():
    nickname = str(input("Input your initials > "))
    score = int(input("Input your score > "))
    return nickname, score


def formatting_data(nickname, score):
    row = f"{nickname} {score}\n"
    return row


def save_file(row):
    with open("savedFile.txt", "a+") as file:
        file.write(row)
        file.close()


def main():
    nickname, score = get_data()
    row = formatting_data(nickname, score)
    save_file(row)
    print("Added to high score table.")


if __name__ == "__main__":
    while True:
        main()
        menu = input("Add another? y/n? ").lower()
        if menu == "n":
            exit()
