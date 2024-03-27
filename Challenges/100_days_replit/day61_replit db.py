import datetime
from replit import db
import time
import os


def clear_display():
    time.sleep(1)
    os.system("clear")


def input_tweet():
    tweet = str(input("Tweet > "))
    return tweet


def add_tweet(tweet):
    timestamp = datetime.datetime.now()
    db[timestamp] = tweet
    print("Tweet Posted 🛫")
    clear_display()


def view_tweet():
    try:
        for key in db.keys():
            print(f"{key} = {db[key]}")
    except:
        print("No tweet yet, go add Tweet!")
        pass


while True:
    menu = input(
        """Tweeter
1: Add Tweet
2: View Tweet
3: Exit
> """
    )

    if menu == "1":
        tweet = input_tweet()
        add_tweet(tweet)
    elif menu == "2":
        view_tweet()
    elif menu == "3":
        exit()
