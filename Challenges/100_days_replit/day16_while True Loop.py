print(
    """
Fill in the blank lyrics!
(Type in the blank lyrics and see if you are as cool as me.)
"""
)
counter = 1
while True:
    verb = input(
        """
Never going to ______ you up.
"""
    )
    if verb == "give":
        print(f"Well done! It only took you {counter} attempts.")
        break
    else:
        counter += 1

# while True:
#   color = input("Enter a color: ")
#   if color == "red":
#     break
#   else:
#     print("Cool color!")
# print("I don't like red")

# counter = 0
# while True:
#   answer = int(input("Enter a number: "))
#   print("Adding it up!")
#   counter += answer
#   print("Current total is", counter)
#   addAnother = input("Add another? ")
#   if addAnother == "no":
#     break
# print("Bye!")

# while True:
#   print("This program is running")
#   goAgain = input("Go again?: ")
#   if goAgain == "no":
#     break
# print("Aww, I was having a good time 😭")
