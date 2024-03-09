print("To-Do List Manager", end="\n\n")

data = []

while True:
    print("Choose an action:")
    print("1. View to-do list")
    print("2. Add a new item")
    print("3. Remove an item")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        if not data:
            print("Your to-do list is empty.\n")
        else:
            print("Your to-do list:")
            for idx, item in enumerate(data, start=1):
                print(f"{idx}. {item}")
            print()

    elif choice == "2":
        task = input("Enter the task you want to add: ")
        data.append(task)
        print(f'Task "{task}" successfully added to the to-do list.\n')

    elif choice == "3":
        if not data:
            print("Your to-do list is already empty.\n")
        else:
            print("Your to-do list:")
            for idx, item in enumerate(data, start=1):
                print(f"{idx}. {item}")
            try:
                idx_to_remove = int(
                    input("Enter the number of the task you want to remove: ")
                )
                if 1 <= idx_to_remove <= len(data):
                    removed_item = data.pop(idx_to_remove - 1)
                    print(
                        f'Task "{removed_item}" has been removed from your to-do list.\n'
                    )
                else:
                    print("Invalid input. Please enter a valid number.\n")
            except ValueError:
                print("Invalid input. Please enter a valid number.\n")

    elif choice == "4":
        print("Thank you for using the To-Do List Manager.")
        break

    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4).\n")
