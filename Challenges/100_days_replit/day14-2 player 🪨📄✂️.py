from getpass import getpass as input

header = "EPIC 🪨 📰 ✂️ BATTLE"

print(f"{header:=^30}\n")
print("Choose your move (R, P, or S)\n")

valid_moves = ["R", "P", "S"]

p1 = input("Player 1 > ")
if p1.upper() not in valid_moves:
    print("Your input must be (R for 🪨, P for 📰, or S for ✂️), try again")
    exit()

p2 = input("Player 2 > ")
if p2.upper() not in valid_moves:
    print("Your input must be (R for 🪨, P for 📰, or S for ✂️), try again")
    exit()

if p1.upper() == p2.upper():
    print("It's a tie, try again!")
elif p1.upper() == "R" and p2.upper() == "P":
    print("Player 1's Rock is covered by Player 2's Paper")
elif p1.upper() == "R" and p2.upper() == "S":
    print("Player 1's Rock crushes Player 2's Scissors")
elif p1.upper() == "P" and p2.upper() == "R":
    print("Player 1's Paper covers Player 2's Rock")
elif p1.upper() == "P" and p2.upper() == "S":
    print("Player 1's Paper is cut by Player 2's Scissors")
elif p1.upper() == "S" and p2.upper() == "P":
    print("Player 1's Scissors cuts Player 2's Paper")
elif p1.upper() == "S" and p2.upper() == "R":
    print("Player 1's Scissors is crushed by Player 2's Rock")
else:
    print("Invalid input, please correct it!")
