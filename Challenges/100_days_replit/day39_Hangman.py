import random

listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]

wordChosen = random.choice(listOfWords)
answer = list("_" * len(wordChosen))

lives = 6

print("🌟Hangman🌟\n\n")

while True:
    if "_" in answer:
        inpt_letter = input("Choose a letter: ")
        if inpt_letter in wordChosen:
            print("Correct!")
            for idx, letter in enumerate(wordChosen):
                if inpt_letter == letter:
                    answer[idx] = letter
            print("".join(answer))
            print()
        else:
            print("Nope, not in there.")
            lives -= 1
            if lives == 0:
                print("You lost!")
                exit()
            print(lives, " left")
            print()

    else:
        print(f"You won with {lives} lives left.")
        exit()
