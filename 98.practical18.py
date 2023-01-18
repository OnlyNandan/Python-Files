my_list = []

while True:
    print("1. Append to list")
    print("2. Remove from list")
    print("3. Insert into list")
    print("4. Sort list")
    print("5. Reverse list")
    print("6. Display list")
    print("7. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        element = input("Enter the element to append: ")
        my_list.append(element)
        print("Element", element, "appended.")
    elif choice == 2:
        element = input("Enter the element to remove: ")
        my_list.remove(element)
        print("Element", element, "removed.")
    elif choice == 3:
        index = int(input("Enter the index to insert at: "))
        element = input("Enter the element to insert: ")
        my_list.insert(index, element)
        print("Element", element, "inserted at index", index)
    elif choice == 4:
        my_list.sort()
        print("List sorted.")
    elif choice == 5:
        my_list.reverse()
        print("List reversed.")
    elif choice == 6:
        print("List:", my_list)
    elif choice == 7:
        break
    else:
        print("Invalid choice.")
