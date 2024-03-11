sentence = input("What sentence do you want rainbow-ising?\n")

color_mapping = {
    "r": "\033[0;31m",  # red
    "y": "\033[33m",  # yellow
    "g": "\033[0;32m",  # green
    "b": "\033[0;34m",  # blue
    "d": "\033[0m",  # default
}

words = sentence.split(" ")
for word in words:
    first_letter = word[0]
    color = color_mapping.get(
        first_letter, color_mapping["d"]
    )  # use default if not in color_mapping
    print(color + word + color_mapping["d"], end=" ")
