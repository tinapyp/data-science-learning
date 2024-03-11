print("🌟Star Wars Name Generator🌟,end=" "\n\n")

first_name = input("Input your first name> ")
last_name = input("Input your lastname > ")
mother_name = input("Input your mother's maiden name > ")
cities = input("Input the city where you were born > ")

star_wars_name = (
    (first_name[:4] + last_name[:4]).capitalize()
    + " "
    + (mother_name[:3] + cities[-3:]).capitalize()
)

print()
print("Your Star Wars name is ", star_wars_name)
