#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
----------------------------------------------------------------------
[•] AUTHOR   : Haroon Sadat
[•] GITHUB   : Afghan Technical
[•] VERSION  : 5.0.0 (Ultimate Automation Hub)
[•] LANGUAGE : English Only
----------------------------------------------------------------------
"""

import os
import sys
import time
import random

# Color Codes for Terminal UI
GREEN = "\033[1;32m"
WHITE = "\033[1;37m"
RED = "\033[1;31m"
CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"

def print_logo():
    """Clears screen and displays the core program banner."""
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
    print(f"{CYAN} [•] Engine   : Hybrid Multi-Thread v5.0")
    print(f"{WHITE}--------------------------------------------------")

class UserAgentDatabase:
    """Contains the massive breakdown list of mobile user-agents seen in the source files."""
    def __init__(self):
        self.agents = [
            "Mozilla/5.0 (Linux; Android 10; Mi 9T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 12; Pixel 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 9; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.119 Mobile Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36",
            "Dalvik/2.1.0 (Linux; U; Android 11; Infinix X6811B)",
            "Dalvik/2.1.0 (Linux; U; Android 10; TECNO KE5)",
            "Mozilla/5.0 (Linux; Android 4.4.2; NX403A Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.93 Mobile Safari/537.36"
        ]
        
    def get_random(self):
        return random.choice(self.agents)

class HaroonMainEngine:
    def __init__(self):
        self.ua_db = UserAgentDatabase()
        self.target_ids = []
        self.ok_list = []
        self.cp_list = []
        self.loop_count = 0
        self.system_key = "HAROON-FREE-TEST-889X"
        
    def check_approval_license(self):
        """Replicates the license/key validator system from the video."""
        print_logo()
        print(f"{YELLOW} [•] Checking System License Status...{WHITE}")
        time.sleep(1)
        
        # Simulating the exact validation logic
        print_logo()
        print(f"{RED} [X] Status: First Get Approval Key!{WHITE}")
        print(f"{WHITE}--------------------------------------------------")
        print(f"{CYAN} [•] Your Registered Key : {YELLOW}{self.system_key}")
        print(f"{WHITE}--------------------------------------------------")
        
        user_name = input(f"{GREEN} [•] Enter Your Name : {WHITE}").strip()
        print(f"{CYAN} [•] Generating API Token for {user_name}...")
        time.sleep(1.5)
        
        print_logo()
        print(f"{GREEN} [✓] License Key Automatically Approved via Server!{WHITE}")
        print(f"{WHITE} Note: Subscription Active for Country Modules.")
        print(f"{WHITE}--------------------------------------------------")
        input(f"{GREEN} Press Enter to launch Main Console...{WHITE}")
        self.main_hub_menu()

    def main_hub_menu(self):
        while True:
            print_logo()
            print(f"{GREEN} [1] Afghanistan Region Modules")
            print(f"{GREEN} [2] Pakistan Region Modules")
            print(f"{RED} [0] Shutdown Automation System")
            print(f"{WHITE}--------------------------------------------------")
            
            option = input(f"{GREEN} Select Terminal Option : {WHITE}").strip()
            
            if option == "1":
                self.operation_gateway_menu("Afghanistan")
            elif option == "2":
                self.operation_gateway_menu("Pakistan")
            elif option == "0":
                print(f"\n{RED} [!] Core disconnected. Goodbye!{WHITE}\n")
                sys.exit()
            else:
                print(f"\n{RED} [!] Selection Error! Try again.{WHITE}")
                time.sleep(1.2)

    def operation_gateway_menu(self, country_name):
        while True:
            print_logo()
            print(f"{YELLOW} [ Active Target Hub : {country_name} ]")
            print(f"{WHITE}--------------------------------------------------")
            print(f"{GREEN} [1] Input Target IDs File (Mass Extract Mode)")
            print(f"{GREEN} [2] Automated API Network Gateway Test")
            print(f"{RED} [B] Back to Main Hub Terminal")
            print(f"{WHITE}--------------------------------------------------")
            
            selection = input(f"{GREEN} Choose Operating System : {WHITE}").strip().upper()
            
            if selection == "1":
                self.process_file_pipeline(country_name)
                break
            elif selection == "2":
                self.process_network_test(country_name)
                break
            elif selection == "B":
                break
            else:
                print(f"\n{RED} [!] Option invalid.{WHITE}")
                time.sleep(1)

    def process_file_pipeline(self, country_name):
        print_logo()
        print(f"{YELLOW} [*] Target Active: {country_name} (File Parsing)")
        file_path = input(f"{GREEN} [•] Input File Path Location (e.g. /sdcard/ids.txt) : {WHITE}").strip()
        
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as stream:
                for line in stream:
                    clean_id = line.strip()
                    if clean_id:
                        self.target_ids.append(clean_id)
            
            total_loaded = len(self.target_ids)
            print_logo()
            print(f"{GREEN} [✓] Stream Verified: {WHITE}{total_loaded} Target Records Injected.")
            print(f"{CYAN} [•] Starting Mbasic Session Layer Simulation for {country_name}...{WHITE}")
            print(f"{WHITE}--------------------------------------------------")
            
            # The core processing simulation layout mimicking the video screen
            for item in self.target_ids:
                self.loop_count += 1
                
                # Instantiating the simulated header data shown at frame 00:12
                current_ua = self.ua_db.get_random()
                simulated_headers = {
                    "host": "mbasic.facebook.com",
                    "accept-language": "en-US,en;q=0.9",
                    "user-agent": current_ua
                }
                
                # Live updates tracker line on terminal
                print(f"\r {WHITE}[Haroon-Engine] {self.loop_count}/{total_loaded} | OK:{GREEN}{len(self.ok_list)}{WHITE} | CP:{RED}{len(self.cp_list)}{WHITE}", end="")
                time.sleep(0.01)
                
            print(f"\n\n{GREEN} [✓] Data parsing session loop finalized successfully.")
            input(f"{WHITE} Press Enter to return to main station...")
            
        except FileNotFoundError:
            print(f"\n{RED} [!] File Processing Error: System could not find path '{file_path}'.")
            time.sleep(3)
            
        # Reset counters for safety memory clear
        self.target_ids = []
        self.loop_count = 0

    def process_network_test(self, country_name):
        print_logo()
        print(f"{GREEN} [*] Establishing handshakes with {country_name} mbasic nodes...{WHITE}")
        time.sleep(1)
        print(f"{CYAN} [•] Extracted User-Agent profiles summary list:{WHITE}")
        for idx in range(1, 4):
            print(f"     {YELLOW}[Profile-{idx}] {WHITE}{self.ua_db.get_random()}")
            time.sleep(0.4)
        print(f"\n{RED} [!] Core processing elements are idling. Ready for operational triggers.{WHITE}")
        input(f"\n{WHITE} Press Enter to return...")

if __name__ == "__main__":
    try:
        engine = HaroonMainEngine()
        engine.check_approval_license()
    except KeyboardInterrupt:
        print(f"\n\n{RED} [!] Execution terminated safely by terminal exit sequence.{WHITE}\n")
        sys.exit()
