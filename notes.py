import helpers

def new_note():
    name = input("Name:\t")
    note = input("Note:\t")
    return (name, note)

def execute():
    helpers.clear_screen()
    print("Notes App")
    execute()