employees = []

while True:
    print("\n1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        emp = {
            "id": input("Enter ID: "),
            "name": input("Enter Name: "),
            "department": input("Enter Department: ")
        }

        employees.append(emp)
        print("Employee added")

    elif choice == "2":
        for emp in employees:
            print(emp)

    elif choice == "3":
        search_id = input("Enter ID to search: ")

        found = False

        for emp in employees:
            if emp["id"] == search_id:
                print(emp)
                found = True

        if not found:
            print("Employee not found")

    elif choice == "4":
        break

    else:
        print("Invalid choice")