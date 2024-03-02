# Answer
print(
    """
MY LOGIN SYSTEM
+++++++++++++++
""",
    end="\n",
)
username = input("Username > ")
password = input("Password > ")

listUser = ["David", "tinApyp", "Arch"]
passUser = ["Secret", "Key", "Password"]

if username in listUser and password in passUser:
    print(
        f"Why hello there {username}, what a lovely accent you have, you could have charmed your way in here even without a password.",
        end="\n",
    )
    print(
        """
  Have a great day

  Don't forget to wear a hat in the sun!
  """
    )
else:
    print("try again tomoorrow guys! ahahaha")

# season = input('what is your favorite season?')
# if season == "spring":
#   print("Ah! The birds are chirping and flowers blooming.")
# elif season == "summer":
#   print("Catch some sun and cool off with a lemonade.")
# elif season == "autumn":
#   print("The leaves are changing and the air is crisp. Enjoy!")
# elif season == "winter":
#   print("Stay warm by the fire and watch the snow fall.")
# else:
#   print("I don't know that season. Please try again.")

# # print("SECURE LOGIN")
# # username = input("Username > ")
# # password = input("Password > ")

# # if username == "mark" and password == 'password':
# #   print("Welcome Mark!")
# # elif username == "fathin" and password == 'rahasia':
# #   print('Welcome my man!')
# # elif username == 'tinapyp' and password == 'secret key':
# #   print('hello my master!')
# # else:
# #   print("Go away!")

# # print("SECURE LOGIN")
# # username = input("Username > ")

# # if username == "mark":
# #   print("Welcome Mark!")

# # else:
# #   print("Go away!")
