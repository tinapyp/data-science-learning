from datetime import datetime

print(
    """
GENERATION INDENTIFIER
++++++++++++++++++++++
"""
)

age = int(
    input(
        """Which year were you born?
"""
    )
)

if age in range(1883 and 1901):
    print("Lost Generation")
elif age in range(1901 and 1928):
    print("Greates Generation")
elif age in range(1928 and 1946):
    print("Silent Generation")
elif age in range(1946 and 1965):
    print("Baby Boomers")
elif age in range(1965 and 1981):
    print("Generation X")
elif age in range(1981 and 1997):
    print("Millenials")
elif age in range(1997 and 2013):
    print("Generaion Z")
elif age in range(2013 and datetime.now().year):
    print("Generaion Z")
else:
    print("oh u come from future, WOW!!")

# score = int(input("What was your score on the test?"))
# if score >= 80:
#   print("Not too shabby")
# elif score > "70":
#   print("Acceptable.")
# else:
#   print("Dude, you need to study more!")

# # myPi = float(input("What is Pi to 3dp?"))
# # if myPi == 3.142 :
# #   print("Exactly!")
# # else:
# #   print("Try again 😭")
