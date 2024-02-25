import os
import sys
import cmd
import socket
import assets.help_command as help_command
import requests
import random
import time
from assets import system_command as cmds_sys
from assets import help_command as cmds_help
from assets.commands import general_commands as cmds
from assets.commands import note as cmds_node

#black = \033[30m
#red = \033[31m
#green = \033[32m
#yellow = \033[33m
#blue = \033[34m
#purple = \033[35m
#cyan = \033[36m
#white = \033[37m
#reset = \033[0m


class MyShell(cmd.Cmd):
    intro = f'\nWelcome to \033[36mUmi\033[0mShell.   Type help or ? to list commands.\n'
    prompt = f"\033[36m{os.getlogin()}@{socket.gethostname()}\033[0m:\033[34m~\033[0m$ "

    def do_help(self, line):
        #List of all commands: HELP
        cmds_help.help()        

    def do_greet(self, line):
        #Greet the user: GREET
        cmds.greet()

    def do_count(self, seconds):
        #count: COUNT <seconds>
        cmds.timer(seconds)
        

    def do_joke(self, line):
        #random joke: JOKE
        cmds.joke()

    def do_note(self, line):
        #open note shell: Note
        cmds_node.note()

    #-------------------system commands-------------------#
        
    def default(self, line):
        self.stdout.write('command:  "%s" not found did you mean\n' % (line,))

    def do_clear(self, line):
        #clear the screen: CLEAR
        cmds_sys.clear()
        

    def do_exit(self, line):
        #Exit the application: EXIT
        cmds_sys.exit()

        
if __name__ == '__main__':
    MyShell().cmdloop()