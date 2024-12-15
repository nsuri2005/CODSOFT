contacts = []

def show_menu():
    print("\nContact Manager")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(contact)
    print("Contact added.")

def view_contacts():
    if len(contacts) == 0:
        print("No contacts available.")
    else:
        index = 1
        for contact in contacts:
            print(str(index) + ". " + contact['name'] + " - " + contact['phone'] + " - " + contact['email'] + " - " + contact['address'])
            index += 1

def search_contact():
    query = input("Enter name or phone to search: ").lower()
    found = []
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            found.append(contact)
    if len(found) == 0:
        print("No matching contact found.")
    else:
        for contact in found:
            print(contact['name'] + " - " + contact['phone'] + " - " + contact['email'] + " - " + contact['address'])

def update_contact():
    view_contacts()
    try:
        index = int(input("Enter the number of the contact to update: ")) - 1
        if index >= 0 and index < len(contacts):
            name = input("Enter new name (leave blank to keep current): ")
            if name != "":
                contacts[index]['name'] = name
            phone = input("Enter new phone (leave blank to keep current): ")
            if phone != "":
                contacts[index]['phone'] = phone
            email = input("Enter new email (leave blank to keep current): ")
            if email != "":
                contacts[index]['email'] = email
            address = input("Enter new address (leave blank to keep current): ")
            if address != "":
                contacts[index]['address'] = address
            print("Contact updated.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input.")

def delete_contact():
    view_contacts()
    try:
        index = int(input("Enter the number of the contact to delete: ")) - 1
        if index >= 0 and index < len(contacts):
            removed = contacts.pop(contacts.pop(index))
            print("Deleted contact: " + removed['name'])
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input.")

while True:
    show_menu()
    choice = input("Choose an option (1-6): ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        break
    else:
        print("Invalid choice.")
