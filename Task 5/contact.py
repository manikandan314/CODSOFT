def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
    print(f"Contact '{name}' added successfully!\n")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.\n")
        return
    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['Phone']}")
    print()

def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details['Phone']:
            print(f"\nContact Found: {name}")
            print(f"Phone: {details['Phone']}, Email: {details['Email']}, Address: {details['Address']}\n")
            found = True
            break
    if not found:
        print("No matching contact found.\n")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print(f"Updating contact '{name}'...")
        phone = input("Enter new phone number (leave blank to keep current): ")
        email = input("Enter new email (leave blank to keep current): ")
        address = input("Enter new address (leave blank to keep current): ")
        if phone:
            contacts[name]['Phone'] = phone
        if email:
            contacts[name]['Email'] = email
        if address:
            contacts[name]['Address'] = address
        print(f"Contact '{name}' updated successfully!\n")
    else:
        print(f"Contact '{name}' not found.\n")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        confirm = input(f"Are you sure you want to delete the contact '{name}'? (yes/no): ").lower()
        if confirm == 'yes':
            del contacts[name]
            print(f"Contact '{name}' deleted successfully!\n")
        else:
            print("Delete operation cancelled.\n")
    else:
        print(f"Contact '{name}' not found.\n")

def main():
    contacts = {}
    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter choice (1/2/3/4/5/6): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")

if __name__ == "__main__":
    main()
