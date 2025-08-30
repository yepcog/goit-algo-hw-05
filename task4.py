# decorator
def input_error(func):
    def inner(*args, **kwargs):

        try:
            return func(*args, **kwargs)
        except TypeError:
            return invalid_args
        except KeyError:
            return "Contact is not on the list."
        except ValueError:
            return "Inappropriate contact Name or phone number."
        except Exception as e:
            return f"{type(e).__name__}: {e}"

    return inner
# end decorator

@input_error
def parse_input(user_input) -> tuple:
    command, *args = user_input.split()
    command = command.strip().casefold()
    return command, *args


# info strings
available_commands = {
                        "hello": "simple greeting command, \
gives advice on how to use 'help' command and why you should consider using it",
                        "exit": "to exit bot assistant and close the program",
                        "help": "provides a list of all available commands \
or information on a specific command by using pattern 'help command'",
                        "all": "provides a list of all saved contacts",
                        "add": "to add new contact to the list of contacts, \
command should match 'add Name phone' pattern",
                        "phone": "provides a phone number of a specific contact, \
command should match 'phone Name' pattern",
                        "change": "to change a phone number for an existing contact, \
command should match 'change Name phone' pattern",
                        "modify": "to modify a Name of an existing contact, \
command should match 'modify Name' pattern",
                        "delete": "to permanently delete a contact from the list of contacts, \
command should match 'delete Name' pattern"
}

invalid_command = "Invalid command."

invalid_args = "Invalid arguments.\n\
You can use 'help command' pattern to verify argument requirements for corresponding command"

hello_str = "How can I help you?\n\
In order to view all available commands you can use 'help' command \
or 'help command' pattern to get information on a specific command"
# end info strings


# command functions
@input_error
def hello_command(*args) -> str:
    return hello_str

@input_error
def exit_command(*args) -> str:
    return "Bye!"

@input_error
def help_command(commands: dict, *args):
    if not args:
        return list(commands.keys())
    other_command, *args = args
    if other_command in commands and not args:
        return f"'{other_command}': '{commands.get(other_command)}'"
    return invalid_command
    

@input_error
def all_command(contacts: dict, *args) -> dict:
    return contacts

@input_error
def add_contact(contacts: dict, name: str, phone: str) -> str:
    if name.isalpha() and int(phone):
        contacts[name] = phone
        return "Contact added."
    return "Inappropriate contact Name or phone number."

@input_error
def show_phone(contacts: dict, name: str) -> str:
    return contacts[name]

@input_error
def change_contact(contacts: dict, name: str, phone: str) -> str:
    if contacts[name] == phone:
        return "This phone number is already associated with corresponding contact."
    for key, value in contacts.items():
        if value == phone:
            return "This phone number is already associated with another contact."
    contacts[name] = phone
    return "Phone number changed."

@input_error
def delete_contact(contacts: dict, name: str) -> str:
    del contacts[name]
    return "Contact deleted."
# end command functions


# invoking
#python task4.py


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "hello":
                print(hello_command(*args))
            case "exit":
                print(exit_command(*args))
                break
            case "help":
                print(help_command(available_commands, *args))
            case "all":
                print(all_command(contacts, *args))
            case "add":
                print(add_contact(contacts, *args))
            case "phone":
                print(show_phone(contacts, *args))
            case "change":
                print(change_contact(contacts, *args))
            case "delete":
                print(delete_contact(contacts, *args))
            case _:
                print(invalid_command)

if __name__ == "__main__":
    main()