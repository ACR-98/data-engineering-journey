#Contacts list
def main():

    import json

    def load_contacts():#Reads the json as a list
        try:
            with open("contacts.json", "r") as contacts_file:
                return json.load(contacts_file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    contacts = load_contacts() #Converts the json into a dict
    def save_contacts(): #Saves a file
        with open("contacts.json", "w") as contacts_file:
            json.dump(contacts, contacts_file, indent=4)
        print("Contacts saved successfully")


    def new_contacts():
        name = input("Enter the name: ").strip()
        number = input("Enter the phone number: ").strip()
        contacts.update({name:number})
        save_contacts()
        print(f"{number} has been added as {name}")

    def view_contacts():
        print("These are your contacts:\n")
        for name, number in contacts.items():
            print(f"{name} : {number}")

    def modify_contacts():
        name = input("Which contact do you want to modify?: ").strip()
        if name in contacts:
            number = input("Enter the new phone number: ").strip()
            contacts[name] = number
            save_contacts()
            print(f"{name}'s phone number has been updated as {number}")  # Corregido ` por '
        else:
            print(f"Contact {name} not found.")

    def search_contacts():
        name = input("Which contact do you want to search?: ").strip()
        if name in contacts:
            print(f"{name}'s phone number is {contacts[name]}")
            else:
            print(f"Contact {name} not found.")

    def exit_contacts():
        choice = str(input("Do you want to exit? (y/n): ").lower()).strip()
        if choice == "y":
            print("Goodbye")
            return True
        if choice == "n":
            return False
        return False

    options = {
        "1":("New contact", new_contacts),
        "2":("View contacts", view_contacts),
        "3":("Modify contacts", modify_contacts),
        "4":("Search contacts", search_contacts),
        "5":("Exit", exit_contacts),
    }

    while True:
        print("\nWelcome to your agenda! ")
        for key, (option, _) in options.items():
            print(f"{key}. {option}")

        try:
            choice = input("\nWhat do you want to do?: ").strip()
            if choice in options:
                _, action = options[choice]
                should_exit = action()
                if should_exit:
                    break
        except ValueError:
            print("Please enter a valid option.")

if __name__ == "__main__":
    main()