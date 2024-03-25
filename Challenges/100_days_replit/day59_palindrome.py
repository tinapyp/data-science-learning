import os


def checker(word):
    reverseWord = word[::-1]
    if word == reverseWord:
        print()
        print(f"{word} is a palindrome. Yay!")
        print()
    else:
        print()
        print("Nope!, it is not")
        print()


while True:
    os.system("clear")
    print("🌟Palindrome Checker🌟")

    word = input("Input a word > ")
    checker(word)
