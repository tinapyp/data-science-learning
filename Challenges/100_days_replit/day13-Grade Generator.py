header = "Exam Grade Calculator"
print(f"{header:=^30}")

exam_name = str(input("Name of Exam: "))
print()
max_score = int(input("Max. Possible Score: "))
print()
user_score = float(input("Your Score: "))
print()

score = user_score / max_score

if score >= 0.9:
    print(f"You got {score:.2%} which is a A+")
elif score >= 0.8:
    print(f"You got {score:.2%} which is a A-")
elif score >= 0.7:
    print(f"You got {score:.2%} which is a B")
elif score >= 0.6:
    print(f"You got {score:.2%} which is a C")
elif score >= 0.5:
    print(f"You got {score:.2%} which is a D")
elif score >= 0.4:
    print(f"You got {score:.2%} which is a U")
else:
    print("Don't Worry u can do it, try again 🏋️")
