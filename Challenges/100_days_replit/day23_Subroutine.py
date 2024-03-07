print("Replit Login System")
print()

userDB = 'tinapyp'
passDB = 'dsaTest'


def login(user, password):
    if user == userDB and password == passDB:
        print("Welcome to Replit!")
        exit()
    else:
        print(
            "Whoops! I don't recognize that username or password. Try again!")


while True:
    user = input("What is your username?: ")
    password = input("what is your password?: ")
    login(user, password)
