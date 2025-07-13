def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
    return inner
    
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact changed."

@input_error
def get_phone(args, contacts):
    name = args[0]
    return contacts[name]

@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts yet."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main():
    contacts = {}
    commands = {
        "add": add_contact,
        "change": change_contact,
        "phone": get_phone,
        "all": lambda args, contacts: show_all(contacts)
        }
    print("Hello! I am your assistant bot.")
    while True:
        user_input = input("Enter a command: ").strip()
        if user_input.lower() in ("exit", "close", "bye"):
         print("Goodbye! See you later!")
        break
        if not user_input:
            print("Enter a command.")
            continue
            parts = user_input.split()
            command = parts[0].lower()
            args = parts[1:]
            handler = commands.get(command)
            if not handler:
                print("Unknown command. Try: add, change, phone, all, exit")
                continue
            result = handler(args, contacts)
            print(result)