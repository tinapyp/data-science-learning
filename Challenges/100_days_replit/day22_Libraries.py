import random

print("Totally Random one-Million-to-one")
print()

number = random.randint(1, 1000000)
counter = 0
print(number)
while True:
    try:
        guess = int(input("What is your guess?: "))
        if guess < number:
            counter = +1
            print("Too low")
        elif guess > number:
            counter = +1
            print("Too High")
        else:
            print(f"Nice one bruh, {counter} attempt!")
            exit()
    except Exception as e:
        print("Error: {}".format(e))
        continue
