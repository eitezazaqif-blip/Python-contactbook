contacts = []
while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == '1':
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        contacts.append({'name': name, 'phone': phone})
        print(f"Contact {name} added.")

    elif choice == '2':
        if contacts:
            print("\nContacts List:")
            for contact in contacts:
                print(f"{contact['name']} | {contact['phone']}")


    elif choice == '3':
        search = input("Enter the name to search: ")
        found = False
        for contact in contacts:
            if contact['name'] == search:
                print(f"{contact['name']} | {contact['phone']}")
                found = True
                break
        if not found:
            print(" not found")

    elif choice == '4':
        delete = input("Enter the name of the contact to delete: ")
        found = False
        for contact in contacts:
            if contact['name'] == delete:
                contacts.remove(contact)
                print("deleted")
                found = True
                break
        if not found:
            print(" not found")

    elif choice == '5':
        print("Exiting the Contact Management System.")
        break

    else:
        print("Invalid option. Please try again.")