import requests
from replit import db


def load_new_joke() -> str:
    """
    Fetch from Joke Api for getting new joke
    """
    results = requests.get(
        "https://icanhazdadjoke.com/", headers={"accept": "application/json"}
    )
    joke_id = results.json()["id"]
    joke = results.json()["joke"]
    return joke_id, joke


def save_joke(joke_id: str, joke: str) -> None:
    db[joke_id] = {"joke_id": joke_id, "joke": joke}
    print("SAVED\n")


def load_joke() -> None:
    for key in db.keys():
        print(db[key]["joke"], "\n")


menu = "(s)ave joke, (l)oad old jokes, (n)ew joke"
joke_id, joke = load_new_joke()
print(joke, "\n")

while True:
    user_input = str(input(f"{menu} > "))
    if user_input == "s":
        save_joke(joke_id, joke)

    elif user_input == "l":
        load_joke()

    elif user_input == "n":
        joke_id, joke = load_new_joke()
        print(joke, "\n")

    else:
        print("See you next time!")
        exit()
