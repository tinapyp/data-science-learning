import time


def read_file():
    contents = []
    with open("high.score", "r") as file:
        for line in file:
            contents.append(line)
    return contents


def highest_score(contents):
    max_score = 0
    max_idx = None

    for idx, row in enumerate(contents):
        score = int(contents[idx][1])
        if score > max_score:
            max_score = score
            max_idx = idx
    return max_idx, max_score


def main():
    print("🌟Current Leader🌟\n")
    print("Analyzing high scores......\n")
    time.sleep(0.2)
    contents = read_file()
    max_idx, max_score = highest_score(contents)
    print(f"Current leader is {contents[max_idx][0]} {max_score}")


if __name__ == "__main__":
    main()
