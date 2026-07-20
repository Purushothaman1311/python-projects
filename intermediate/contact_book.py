contacts = {}

while True:
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6):")

    if choice == "1":
        name = input("Enter Name:")
        phone = input("Enter Phone Number:")

        if name in contacts:
            print("Contact already exists!")
        else:
            contacts[name] = phone
            print("Contact added successfully.")

    elif choice == "2":
        if contacts:
            print("\n--- Contact List ---")
            for name, phone in contacts.items():
                print(f"Name: {name}, Phone: {phone}")
        else:
            print("No contacts found.")

    elif choice == "3":
        name = input("Enter Name to Search:")

        if name in contacts:
            print(f"Phone Number: {contacts[name]}")
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter Name to Update:")

        if name in contacts:
            new_phone = input("Enter New Phone Number:")
            contacts[name] = new_phone
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    elif choice == "5":
        name = input("Enter Name to Delete:")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    elif choice == "6":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")



