contacts = {}
def add_contact(name, number):
    contacts[name] = number
    print(f"Contact '{name}' added successfully with number '{number}'.")
    
def search_contact(name):
    if name in contacts:
        print(f"Name: {name}, Number: {contacts[name]}")
    else:
        print(f"Contact '{name}' not found.")

def view_contacts():
    if contacts:
        print("Contacts:")
        for name, number in contacts.items():
            print(f"Name: {name}, Number: {number}")
    else:
        print("No contacts found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

while True:
    print("\nWelcome to the Contact Book!")
    print("1. Add a new contact")
    print("2. Search for a contact")
    print("3. View all contacts")
    print("4. Delete a contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        add_contact(name, number)

    elif choice == '2':
        name = input("Enter name to search: ")
        search_contact(name)

    elif choice == '3':
        view_contacts()

    elif choice == '4':
        name = input("Enter name to delete: ")
        delete_contact(name)

    elif choice == '5':
        print("Thank you for using the Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
