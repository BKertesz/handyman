import helpers, notes

def help():
    print("You can use the following programs:")
    for k in programs.keys():
        print(k)

def test():
    result = helpers.prompt("Yes or No?")
    print(result)

programs = {
    "help": help,
    "clear": helpers.clear_screen,
    "notes": notes.execute,
    "exit": exit,
    "test": test
}

def main():
    program_number = input(">> ").lower()
    func = programs.get(program_number, lambda: print("Invalid program try help"))
    func()
    main()

if __name__ == "__main__":
    helpers.clear_screen()
    print("Welcome to HandyMan")
    main()