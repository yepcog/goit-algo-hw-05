import sys


# decorator
def input_error(func):
    def inner(command, *args):

        # "hello" DONE (except e)
        if command == "hello":
            if args:
                return invalid_command
            try:
                return func(command, *args)
            except Exception as e: # BAD PRACTICE, i can change it later tho
                return f"{type(e).__name__}: {e}"

        # "exit" DONE (except e)
        if command == "exit":
            if args:
                return invalid_command
            try:
                return func(command, *args)
            except Exception as e:
                return f"{type(e).__name__}: {e}"

        # "help" DONE (except e)
        if command == "help":
            try:
                available_commands, *args = args
                if args.__len__() == 1:
                    other_command = " ".join(args)
                    return f"'{other_command}': '{available_commands.get(other_command)}'"
                elif args == []:
                    return func(command, available_commands)
                else:
                    return invalid_command
            except Exception as e:
                return f"{type(e).__name__}: {e}"

        # "all" DONE (except e)
        if command == "all":
            contacts, *args = args
            if args != []:
                return invalid_args
            try:
                return func(command, contacts)
            except Exception as e:
                return f"{type(e).__name__}: {e}"

        # "add" DONE (except e)
        if command == "add":
            contacts, *args = args
            if args.__len__() == 2:
                try:
                    name, phone = arg_sep(args)
                    if name in contacts:
                        return "Contact is already registered."
                    for key, value in contacts.items():
                        if value == phone:
                            return "This phone number is already associated with another contact."
                    return func(command, contacts, args)
                except ValueError:
                    return invalid_args
                except Exception as e:
                    return f"{type(e).__name__}: {e}"
            else:
                return invalid_args
        
        # "phone" DONE (except e)
        if command == "phone":
            contacts, *args = args
            if args.__len__() == 1:
                try:
                    name = " ".join(args)
                    if name.isdigit():
                        return invalid_args
                    elif name not in contacts:
                        return "Contact is not on the list."
                    return func(command, contacts, name)
                except Exception as e:
                    return f"{type(e).__name__}: {e}"
            else:
                return invalid_args
            
        # "change" DONE (except e)
        if command == "change":
            contacts, *args = args
            if args.__len__() == 2:
                try:
                    name, phone = arg_sep(args)
                    if name not in contacts:
                        return "Contact is not on the list."
                    elif contacts[name] == phone:
                        return "This phone number is already associated with corresponding contact."
                    for key, value in contacts.items():
                        if value == phone:
                            return "This phone number is already associated with another contact."
                    return func(command, contacts, args)
                except ValueError:
                    return invalid_args
                except TypeError:
                    return invalid_args
                except Exception as e:
                    return f"{type(e).__name__}: {e}"
            else:
                return invalid_args

        # "modify" DONE (except e), still messy btw
        if command == "modify":
            contacts, *args = args
            if args.__len__() == 1:
                try:
                    old_name = " ".join(args)
                    if old_name.isdigit():
                        return invalid_args
                    elif old_name not in contacts:
                        return "Contact is not on the list."
                    elif old_name in contacts:
                        while True:
                            new_name = input("Enter a new Name: ")
                            if new_name.split().__len__() == 1 and new_name.isdigit() == False:
                                try:
                                    if new_name.strip() in ["hello", "exit", "help", "all", "add", "phone", "change", "modify", "delete"]:
                                        if new_name.strip() == "exit":
                                            return "Contact modification cancelled."
                                        print(modify_str)
                                        continue
                                    elif new_name in contacts:
                                        print("Contact with this name is already registered.")
                                        continue
                                    else:
                                        return func(command, contacts, old_name, new_name)
                                except ValueError:
                                    print("To modify a contact's Name, a new Name must be provided.\n\
You can use 'exit' command to cancel contact modification")
                                    continue
                                except Exception as e:
                                    print(f"{type(e).__name__}: {e}")
                                    continue
                            else:
                                print(modify_str)
                                continue
                except Exception as e:
                    return f"{type(e).__name__}: {e}"
            else:
                return invalid_args

        # "delete" DONE (except e)
        if command == "delete":
            contacts, *args = args
            if args.__len__() == 1:
                try:
                    name = " ".join(args)
                    if name.isdigit():
                        return invalid_args
                    return func(command, contacts, name)
                except KeyError:
                    return "Contact is not on the list."
                except Exception as e:
                    return f"{type(e).__name__}: {e}"
            else:
                return invalid_args

        if Exception:
            return invalid_command

    return inner
# end decorator

@input_error
def parse_input(user_input) -> tuple:
    command, *args = user_input.split()
    command = command.strip().casefold()
    return command, *args

def arg_sep(args) -> tuple:
	name = ""
	phone = ""
	for arg in args:
		if phone != "" and arg.isalpha():
			return invalid_args
		elif arg.isalpha():
			name = arg
		elif arg.isdigit():
			phone = arg
		else:
			return "Inappropriate contact Name or phone number."
	if phone == "":
		return invalid_args
	return name, phone


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

invalid_command = "Invalid command.\n\
You can use 'help' command or 'help command' pattern to verify argument requirements for corresponding command"

invalid_args = "Arguments don't match a command pattern.\n\
You can use 'help' command or 'help command' pattern to verify argument requirements for corresponding command"

hello_str = "How can I help you?\n\
In order to view all available commands you can use 'help' command \
or 'help command' pattern to get information on a specific command"

modify_str = "Inappropriate contact Name.\n\
You can use 'exit' command to cancel contact modification"
# end info strings


# command functions
@input_error
def hello_command(command: str, *args) -> str:
    return hello_str

@input_error
def exit_command(command: str, *args) -> None:
    print("Bye!")
    return sys.exit(0)

@input_error
def help_command(command: str, commands: dict, *args):
    return list(commands.keys())

@input_error
def all_command(command: str, contacts: dict, *args) -> dict:
    return contacts

@input_error
def add_contact(command: str, contacts: dict, args) -> str:
    name, phone = arg_sep(args)
    contacts[name] = phone
    return "Contact added."

@input_error
def show_phone(command: str, contacts: dict, name: str) -> str:
    return contacts.get(name)

@input_error
def change_contact(command: str, contacts: dict, args) -> str:
    name, phone = arg_sep(args)
    contacts[name] = phone
    return "Phone number changed."

@input_error
def modify_contact(command: str, contacts: dict, old_name: str, new_name: str) -> str:
    phone = contacts.pop(old_name)
    contacts[new_name] = phone
    return "Contact modified."

@input_error
def delete_contact(command: str, contacts: dict, name: str) -> str:
    del contacts[name]
    return "Contact deleted."
# end command functions


# invoking
#python my_task4.py


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "hello": # DONE
                print(hello_command(command, *args))
            case "exit": # DONE
                print(exit_command(command, *args))
            case "help": # DONE
                print(help_command(command, available_commands, *args))
            case "all": # DONE
                print(all_command(command, contacts, *args))
            case "add": # DONE
                print(add_contact(command, contacts, *args))
            case "phone": # DONE
                print(show_phone(command, contacts, *args))
            case "change": # DONE
                print(change_contact(command, contacts, *args))
            case "modify": # DONE
                print(modify_contact(command, contacts, *args))
            case "delete": # DONE
                print(delete_contact(command, contacts, *args))
            case _:
                print(invalid_command)

if __name__ == "__main__":
    main()