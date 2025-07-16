def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    with open("contacts.txt", "a") as file:
        file.write(f"{name},{phone},{email}\n")
    print("✅ Contact added successfully.\n")


def view_contacts():
    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()
            if contacts:
                print("\n📒 All Contacts:")
                for contact in contacts:
                    name, phone, email = contact.strip().split(",")
                    print(f"Name: {name}, Phone: {phone}, Email: {email}")
            else:
                print("📭 No contacts found.")
    except FileNotFoundError:
        print("📁 Contact file does not exist yet.")


def search_contact():
    search_name = input("Enter name to search: ").lower()
    found = False
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                name, phone, email = line.strip().split(",")
                if search_name in name.lower():
                    print(f"\n🔍 Found Contact -> Name: {name}, Phone: {phone}, Email: {email}")
                    found = True
        if not found:
            print("❌ Contact not found.")
    except FileNotFoundError:
        print("📁 Contact file does not exist yet.")


def main():
    while True:
        print("\n📞 Contact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
