import cmd
import os
from assets.commands import general_commands as cmds
from assets import help_command as cmds_help
from assets import system_command as cmds_sys
def note():

    pat = "C:/Users/disco/OneDrive/Bureaublad/overig/programeren/Python/fun projects/UmiShell/assets/notes"

    class MyShell(cmd.Cmd):
        intro = f'\n\n*---------------------------------------*\n| Welcome to the \033[36mUmi\033[0mShell Sticky Note App |\n*---------------------------------------*\n\n'
        prompt = "note >>> "

        def do_help(self, line):
            cmds_help.note_help()

        def do_create(self, name):
            name = name.lower()
            name = name.replace(' ', '-')
            file_path = f"{pat}/{name}.txt"

            print("Enter the content of your note. to exit use Ctrl + z and to go to the next line use ENTER:")
            lines = []
            while True:
                try:
                    line = input()
                except EOFError:
                    break
                lines.append(line)
            
            with open(file_path, 'w') as file:
                file.write('\n'.join(lines))
    
            print(f"Note '{name}' has been created.")

        def do_read(self, name):
            name = name.replace(' ', '-')
            file_path = f"{pat}/{name}.txt"
            
            if os.path.isfile(file_path):
                with open(file_path, 'r') as file:
                    print(file.read())
            else:
                print(f"Note '{name}' does not exist.")

        def do_delete(self, name):
            name = name.replace(' ', '-')
            file_path = f"{pat}/{name}.txt"
            
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Note '{name}' has been deleted.")
            else:
                print(f"Note '{name}' does not exist.")
        
        def do_list(self, line):

            def get_files_in_directory(directory_path):
                files = []
                for f in os.listdir(directory_path):
                    if os.path.isfile(os.path.join(directory_path, f)):
                        files.append(f)
                return files

            files = get_files_in_directory(pat)
            my_string = "\n".join(files)
            my_string = my_string.replace('.txt', '')
            print(f"List of all notes:\n\033[33m{my_string}\033[0m")

        def do_clear(self, line):
            cmds_sys.clear()

        def do_exit(self, line):
            return True

    MyShell().cmdloop()