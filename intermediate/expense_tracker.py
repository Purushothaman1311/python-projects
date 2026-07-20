expenses = {}

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Update Expense")
    print("5. Delete Expense")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        expense_id = input("Enter Expense ID: ")

        if expense_id in expenses:
            print("Expense ID already exists!")
        else:
            category = input("Enter Category (Food, Travel, Shopping, etc.): ")
            amount = float(input("Enter Amount: "))
            date = input("Enter Date (DD-MM-YYYY): ")

            expenses[expense_id] = {
                "Category": category,
                "Amount": amount,
                "Date": date
            }

            print("Expense added successfully.")

    elif choice == "2":
        if expenses:
            print("\n----- Expense List -----")
            total = 0

            for expense_id, details in expenses.items():
                print(f"\nExpense ID : {expense_id}")
                print(f"Category   : {details['Category']}")
                print(f"Amount     : ₹{details['Amount']}")
                print(f"Date       : {details['Date']}")

                total += details["Amount"]

            print(f"\nTotal Expenses: ₹{total}")
        else:
            print("No expenses found.")

    elif choice == "3":
        expense_id = input("Enter Expense ID to Search: ")

        if expense_id in expenses:
            details = expenses[expense_id]
            print("\nExpense Found")
            print(f"Expense ID : {expense_id}")
            print(f"Category   : {details['Category']}")
            print(f"Amount     : ₹{details['Amount']}")
            print(f"Date       : {details['Date']}")
        else:
            print("Expense not found.")

    elif choice == "4":
        expense_id = input("Enter Expense ID to Update: ")

        if expense_id in expenses:
            category = input("Enter New Category: ")
            amount = float(input("Enter New Amount: "))
            date = input("Enter New Date (DD-MM-YYYY): ")

            expenses[expense_id] = {
                "Category": category,
                "Amount": amount,
                "Date": date
            }

            print("Expense updated successfully.")
        else:
            print("Expense not found.")

    elif choice == "5":
        expense_id = input("Enter Expense ID to Delete: ")

        if expense_id in expenses:
            del expenses[expense_id]
            print("Expense deleted successfully.")
        else:
            print("Expense not found.")

    elif choice == "6":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")
