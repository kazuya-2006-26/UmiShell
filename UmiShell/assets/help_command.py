commands = {
    "help": "- help: List of all commands | help",
    "greet": "- greet: Greet the world | greet",
    "timer": "- timer: Set a timer | timer <seconds>",
    "joke": "- joke: Tell a random joke | joke",
    "note": "- note: Open the note shell | note",
    "clear": "- clear: Clear the terminal | clear",
    "exit": "- exit: Exit the application | exit",
}

note_commands = {
    "help": "- help: list of all commands | help",
    "create": "- create: Create a new note | create <name>",
    "read": "- read: Read a note | read <name>",
    "delete": "- delete: Delete a note | delete <name>",
    "list": "- list: A list with all the notes | list",
}

def help():
    print("List of all commands:")
    print("====================================")
    List = list(commands.values())
    for items in List:
        print(items)

def note_help():
    print("List of all commands:")
    print("====================================")
    List = list(note_commands.values())
    for items in List:
        print(items)