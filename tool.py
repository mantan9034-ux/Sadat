#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Haroon Sadat
Github: Afghan Technical
Description: A professional cloning and file management utility tool.
"""

import os
import sys
import time

# ANSI Color Codes for Terminal
GREEN = "\033[1;32m"
WHITE = "\033[1;37m"
RED = "\033[1;31m"
CYAN = "\033[1;36m"

def display_logo():
    os.system("clear" if os.name == "posix" else "cls")
    print(f"""{GREEN}
$$\   $$\  $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ 
$$ |  $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$ |  $$ |
$$ |  $$ |$$ /  $$ |$$ |  $$ |$$ /  $$ |$$ /  $$ |$$ |  $$ |
$$$$$$$$ |$$$$$$$$ |$$$$$$$  |$$ |  $$ |$$ |  $$ |$$$$$$$$ |
$$  __$$ |$$  __$$ |$$  __$$< $$ |  $$ |$$ |  $$ |$$  __$$ |
$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |
$$ |  $$ |$$ |  $$ |$$ |  $$ | $$$$$$  | $$$$$$  |$$ |  $$ |
\__|  \__|\__|  \__|\__|  \__| \______/  \______/ \__|  \__|
    """)
    print(f"{WHITE}--------------------------------------------------")
    print(f"{CYAN} [•] Author   : Haroon Sadat")
    print(f"{CYAN} [•] Github   : Afghan Technical")
    print(f"{CYAN} [•] Version  : 1.0.0")
    print(f"{WHITE}--------------------------------------------------")

class HaroonTool:
    def __init__(self):
        self.file_list = []
        self.status_ok = []
        self.status_cp = []
        self.loop_counter = 0
        self.execute_menu()

    def execute_menu(self):
        while True:
            display_logo()
            print(f"{GREEN} [1] File Cloning")
            print(f"{GREEN} [2] Public Cloning")
            print(f"{GREEN} [3] Create File")
            print(f"{GREEN} [4] 2008-2009 Cloning")
            print(f"{RED} [0] Exit Tool")
            print(f"{WHITE}--------------------------------------------------")
            
            try:
                choice = input(f"{GREEN} Select Option : {WHITE}").strip()
                
                if choice == "1":
                    self.file_cloning()
                elif choice == "2":
                    self.public_cloning()
                elif choice == "3":
                    self.create_file()
                elif choice == "4":
                    self.old_cloning()
                elif choice == "0":
                    print(f"\n{RED} [!] Exiting tool. Thank you for using!{WHITE}\n")
                    sys.exit()
                else:
                    print(f"\n{RED} [!] Invalid choice. Please select from the menu.{WHITE}")
                    time.sleep(2)
            except KeyboardInterrupt:
                print(f"\n{RED} [!] Tool interrupted by user.{WHITE}\n")
                sys.exit()

    def file_cloning(self):
        display_logo()
        print(f"{GREEN} [*] Launching File Cloning Module...{WHITE}")
        input(f"\n{WHITE} Press Enter to return to main menu...")

    def public_cloning(self):
        display_logo()
        print(f"{GREEN} [*] Launching Public Cloning Module...{WHITE}")
        input(f"\n{WHITE} Press Enter to return to main menu...")

    def create_file(self):
        display_logo()
        print(f"{GREEN} [*] Launching File Creation Module...{WHITE}")
        input(f"\n{WHITE} Press Enter to return to main menu...")

    def old_cloning(self):
        display_logo()
        print(f"{GREEN} [*] Launching 2008-2009 Cloning Module...{WHITE}")
        input(f"\n{WHITE} Press Enter to return to main menu...")

if __name__ == "__main__":
    HaroonTool()
