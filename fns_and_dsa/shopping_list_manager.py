def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            shopping_list.append(input("Enter an item name"))
            print("Your item has been added")
            pass
        elif choice == '2':
            item = input("Please enter the item name")
            if item in shopping_list:
                shopping_list.remove(item)
                print("item has been removed succseffulley")
            else:
                print("item doesnt exist in the list")
            pass
        elif choice == '3':
            print(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
