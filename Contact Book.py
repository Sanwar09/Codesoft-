contacts = []
def add_contact(name, phone, email, address):
    contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
    print("Contact added successfully.")

def view_contact_list():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contact List:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}")

def search_contact(keyword):
    found_contacts = []
    for contact in contacts:
        if keyword.lower() in contact['name'].lower() or keyword in contact['phone']:
            found_contacts.append(contact)
    if not found_contacts:
        print("No contacts found.")
    else:
        print("Search results:")
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")

def update_contact(name, phone, email, address):
    for contact in contacts:
        if contact['name'] == name:
            contact['phone'] = phone
            contact['email'] = email
            contact['address'] = address
            print("Contact updated successfully.")
            return
    print("Contact not found.")

def delete_contact(name):
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            print("Contact deleted successfully.")
            return
    print("Contact not found.")

print("-\n--------Welcome to Contact Management System!---------")

while True:
    print('''
                  \nMenu:
                  1.Add Contacts
                  2.View Contact List
                  3.Search Contact
                  4.Update Contact
                  5.Delete Contact
                  6.Exit
    ''')

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        add_contact(name, phone, email, address)
    elif choice == '2':
        view_contact_list()
    elif choice == '3':
        keyword = input("Enter name or phone number to search: ")
        search_contact(keyword)
    elif choice == '4':
        name = input("Enter name of contact to update: ")
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")
        update_contact(name, phone, email, address)
    elif choice == '5':
        name = input("Enter name of contact to delete: ")
        delete_contact(name)
    elif choice == '6':
        print("Goodbye! and Thank You for Visiting Again🙏🙏🙏")
        break
    else:
        print("Invalid choice. Please try again.")
