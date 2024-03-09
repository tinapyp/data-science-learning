def color(color=None):
    if color == "red":
        return "\033[0;31m"
    elif color == "blue":
        return "\033[0;34m"
    elif color == "white":
        return "\033[0;37m"
    elif color == "yellow":
        return "\033[0;33m"
    elif color == "green":
        return "\033[0;32m"
    elif color == "black":
        return "\033[0;30m"
    else:
        return "\033[0m"


print(
    f'{color("red")}={color("white")}={color("blue")}={color("yellow")} Music App {color("blue")}={color("white")}={color("red")}=',
    end="\n\n",
)
print("🔥🔘", f'{color("white")}Radio Gaga')
print(" " * 4 + f'{color("yellow")} Queen')
print(f'{color("white")}PREV')
print(" " * 5 + f'{color("green")}NEXT')
print(" " * 9 + f'{color("red")}PAUSE', end="\n\n\n")

print("WELCOME TO".center(42))
print(f'{color("blue")}--- ARM BOOK ---'.center(50), end="\n\n")

text = """
Definitely not a rip off of
a certain other social
networking site
"""
print(f'{color("yellow")}{text:>50}')

print(f'{color("red")}Honest.'.center(50))

text = "Username: "
print(f'{color("white")}{text:^42}', end="")
entered_username = input()

text = "Password: "
print(f'{color("white")}{text:^42}', end="")
entered_username = input()
