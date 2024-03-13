import random, os, time


def clear_workspace():
    time.sleep(0.5)
    os.system("clear")


def saved_data(input):
    with open("idea.txt", "a+") as file:
        file.write(input + "\n")
        file.close()
        print("Added idea into Second Brain")
        clear_workspace()


def read_data():
    ideas = []
    with open("idea.txt", "r") as file:
        for line in file:
            ideas.append(line)
    return ideas


def random_idea(data):
    i = random.randint(0, len(data))
    idea = data[i]
    return idea


print("Second Brain Idea DB")
while True:
    try:
        menu = input(
            """
Menu:
1. Add Idea to Second Brain
2. Choose Random Idea from Second Brain
3. Exit
> """
        )

        if menu == "1":
            print("Add Idea\n")
            idea = input("> ")
            saved_data(idea)
        elif menu == "2":
            ideas = read_data()
            idea = random_idea(ideas)
            print(f"Random Idea: {idea}")
            menu = input("Back to menu? (y/n)")
            if menu == "y":
                clear_workspace()
            else:
                exit()
        elif menu == "3":
            exit()

    except Exception as e:
        print(f"Error: {e}")
        continue
