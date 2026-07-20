library = {}

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        book_id = input("Enter Book ID: ")

        if book_id in library:
            print("Book already exists!")
        else:
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")

            library[book_id] = {
                "Title": title,
                "Author": author
            }

            print("Book added successfully.")

    elif choice == "2":
        if library:
            print("\n----- Book List -----")
            for book_id, details in library.items():
                print(f"\nBook ID : {book_id}")
                print(f"Title   : {details['Title']}")
                print(f"Author  : {details['Author']}")
        else:
            print("No books available.")

    elif choice == "3":
        book_id = input("Enter Book ID to Search: ")

        if book_id in library:
            details = library[book_id]
            print("\nBook Found")
            print(f"Book ID : {book_id}")
            print(f"Title   : {details['Title']}")
            print(f"Author  : {details['Author']}")
        else:
            print("Book not found.")

    elif choice == "4":
        book_id = input("Enter Book ID to Update: ")

        if book_id in library:
            title = input("Enter New Book Title: ")
            author = input("Enter New Author Name: ")

            library[book_id] = {
                "Title": title,
                "Author": author
            }

            print("Book updated successfully.")
        else:
            print("Book not found.")

    elif choice == "5":
        book_id = input("Enter Book ID to Delete: ")

        if book_id in library:
            del library[book_id]
            print("Book deleted successfully.")
        else:
            print("Book not found.")

    elif choice == "6":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")
