"""module with functions for parsing commands and adding contacts"""

from handlers import *

from phonebook_control import AddressBook


def main():
    """function for starting and/or stopping bot-app"""
    contacts = AddressBook()
    print("😎 Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("😊 Good bye!")
            break
        elif command == "hello":
            print("🤓 How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "add-birthday":
            print(add_birthday(args, contacts))
        elif command == "show-birthday":
            print(show_birthday(args, contacts))
        elif command == "birthdays":
            print(birthdays(contacts))
        else:
            print("🫣 Invalid command.")


if __name__ == "__main__":
    main()
