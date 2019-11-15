import os

clear_screen = lambda: os.system("clear")
save_file = lambda filename, content: save_file_with_mode(filename, "a", content) if os.path.isfile() else save_file_with_mode(filename, "w", content)
delete_file = lambda filename: os.remove(filename)
prompt = lambda question: True if input(question + "\t[y/n]\t").lower() == "y" else False

def save_file_with_mode(filename, mode, content):
    with open(filename, mode) as file:
        file.write(content)

def execute_program(program_dictionary, selection):
    