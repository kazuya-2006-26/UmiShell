import os

def exit():
    print("Thanks for using my shell. Goodbye!")
    return True

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear') 