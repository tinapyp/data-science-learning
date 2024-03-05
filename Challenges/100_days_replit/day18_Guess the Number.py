counter = 0
number = 600000
gob = ""
print("One-Million-To-One")
while True:
    guess = int(input("What is you guess: "))
    counter += 1
    if guess < 0:
        exit()
    elif guess < number:
        print("Too low")
    elif guess > number:
        print("Too big")
    else:
        print("It took you {} guess to get it correct".format(counter))
