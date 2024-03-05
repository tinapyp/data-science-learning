from getpass import getpass as input

header = "MOST EPIC 🪨 📰 ✂️ BATTLE"

print(f"{header:=^30}\n")
print("Choose your move (R, P, or S)\n")

valid_moves = ["R", "P", "S"]

round = 1
score_p1 = 0
score_p2 = 0
while True:
    print()
    print(f"Round {round}")
    print()

    if score_p1 == 2:
        print(f"Player 1 wins with {score_p1} victories")
        break
    elif score_p2 == 2:
        print(f"Player 2 wins with {score_p2} victories")
        break

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
        score_p2 += 1
        print("Player 1's Rock is covered by Player 2's Paper")
    elif p1.upper() == "R" and p2.upper() == "S":
        score_p1 += 1
        print("Player 1's Rock crushes Player 2's Scissors")
    elif p1.upper() == "P" and p2.upper() == "R":
        print("Player 1's Paper covers Player 2's Rock")
        score_p1 += 1
    elif p1.upper() == "P" and p2.upper() == "S":
        print("Player 1's Paper is cut by Player 2's Scissors")
        score_p2 += 1
    elif p1.upper() == "S" and p2.upper() == "P":
        print("Player 1's Scissors cuts Player 2's Paper")
        score_p1 += 1
    elif p1.upper() == "S" and p2.upper() == "R":
        print("Player 1's Scissors is crushed by Player 2's Rock")
        score_p2 += 1
    else:
        print("Invalid input, please correct it!")
    round += 1

# print("Let's play chutes and ladders. Pick ladder or chute.")
# while True:
#   print("Do you want to go up the ladder or down the chute?")
#   direction = input("> ")
#   if direction == "chute":
#     print("Game over!")
#     break
#   elif direction == "ladder":
#       continue
#   else:
#       print("Game over!")
#       exit()
# print("Thanks for playing!")

# while True:
#     print("You are in a corridor, do you go left or right?")
#     direction = input("> ")
#     if direction == "left":
#         print("You have fallen to your death")
#         break
#     elif direction == "right":
#         continue  # going back into first statement
#     else:
#         print("Ahh! You're a genius, you've won")
#         exit()
# print('The game is over, you\'ve failed!')
