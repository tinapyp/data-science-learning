name = []

while True:
    fName = input("First Name: ").strip().capitalize()
    lName = input("Last Name: ").strip().capitalize()
    print()

    full_name = fName + " " + lName
    if full_name in name:
        print("ERROR: Duplicate name")
    else:
        name.append(full_name)
        print(full_name)
        print()
