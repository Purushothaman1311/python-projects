students = {}

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        roll_no = input("Enter Roll Number: ")

        if roll_no in students:
            print("Student already exists!")
        else:
            name = input("Enter Student Name: ")
            age = input("Enter Age: ")
            course = input("Enter Course: ")

            students[roll_no] = {
                "Name": name,
                "Age": age,
                "Course": course
            }

            print("Student added successfully.")

    elif choice == "2":
        if students:
            print("\n----- Student List -----")
            for roll_no, details in students.items():
                print(f"\nRoll No : {roll_no}")
                print(f"Name    : {details['Name']}")
                print(f"Age     : {details['Age']}")
                print(f"Course  : {details['Course']}")
        else:
            print("No student records found.")

    elif choice == "3":
        roll_no = input("Enter Roll Number to Search: ")

        if roll_no in students:
            details = students[roll_no]
            print("\nStudent Found")
            print(f"Roll No : {roll_no}")
            print(f"Name    : {details['Name']}")
            print(f"Age     : {details['Age']}")
            print(f"Course  : {details['Course']}")
        else:
            print("Student not found.")

    elif choice == "4":
        roll_no = input("Enter Roll Number to Update: ")

        if roll_no in students:
            name = input("Enter New Name: ")
            age = input("Enter New Age: ")
            course = input("Enter New Course: ")

            students[roll_no] = {
                "Name": name,
                "Age": age,
                "Course": course
            }

            print("Student updated successfully.")
        else:
            print("Student not found.")

    elif choice == "5":
        roll_no = input("Enter Roll Number to Delete: ")

        if roll_no in students:
            del students[roll_no]
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    elif choice == "6":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")
