# Part B - Shopping List Manager

shopping = []

while True:
    choice = input("add / remove / show / done: ").strip().lower()

    if choice == "add":
        item = input("Item to add: ").strip()
        if item:
            shopping.append(item)
            print(f"Added {item}.")
        else:
            print("Please type an item name.")

    elif choice == "remove":
        item = input("Item to remove: ").strip()
        if item in shopping:
            shopping.remove(item)
            print(f"Removed {item}.")
        else:
            print("That item is not on your list.")

    elif choice == "show":
        if not shopping:
            print("Your list is empty.")
        else:
            for item in shopping:
                print(item)

    elif choice == "done":
        print("Goodbye! Happy shopping.")
        break

    else:
        print("Please choose add, remove, show or done.")