print("Marvel Movie Character Creator")
print("--", end="\n")

spider = input("Do you like 'hanging around'? ")
if spider.lower() == "no":
    print("Then you are not a Spider-man")
    korg = input("Do you have a 'gravelly' voice?: ")
    if korg.lower() == "no":
        print("Aww, then you are not a Korg")
        captain = input("Do you feel 'Marvelous'? ")
        if captain.lower() == "no":
            print("so you not Captain too, who are you dude? ")
        else:
            print("Aha! You are Captain Marvel! Hi!")
    else:
        print("Aha! You are Korg! Hi!")
else:
    print("Aha! You are Spider-man! Hi!")

# myName = input('What is your name dude? ')
# if myName.lower() == 'fathin':
#   print('u are so handsome bruh')
# else:
#   print('bruh that not your i want to see')

# catsOrDogs = input("Are you a cat person? Or a dog person?: ")
# if catsOrDogs == "cat":
#   print("Meow")
# else:
#   print("Woof")

# drink = input("Do you prefer coffee or tea?")
# if drink == "coffee":
#   print("Tea is better.")
# else:
#   print("Excellent choice.")
