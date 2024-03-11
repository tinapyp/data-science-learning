print("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾")

element_colors = {
    "earth": "\033[0;33m",  # ANSI color code for yellow
    "fire": "\033[0;31m",  # ANSI color code for red
    "air": "\033[0;36m",  # ANSI color code for cyan
    "water": "\033[0;34m",  # ANSI color code for blue
    "spirit": "\033[0;35m",  # ANSI color code for magenta
}

beast_deck = {"name": None, "type": None, "move": None, "hp": None, "mp": None}

name = input("Input your beast's name > ")
type = input("Input your beast's type > ")
move = input("Input your beast's special move > ")
hp = input("Input your beast's staring HP > ")
mp = input("Input your beast's staring MP > ")

color = element_colors.get(type, "\033[0m")
text = (
    f"Your beast is called {name}. It is an {type} beast with a special move of {move}"
)
print(f"{color}{text}")
