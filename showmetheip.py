import requests
from colorama import Fore, Back, init
import os
import platform
import time
import ipaddress
import json
from pystyle import Center, Cursor

def requesting(IP):
    url = f"http://ip-api.com/json/{IP}"
    try: 
        getin = requests.get(url)
        if getin.status_code == 204:
            print(Fore.LIGHTGREEN_EX + "[+] Successful request")
        elif getin.status_code == 403:
            print(Fore.LIGHTRED_EX + "[!] Unsuccessful request: 403")
            return
        data = getin.json()
        print(Fore.LIGHTGREEN_EX + "[+] IP Information Retrieved:\n")
        print(f"  IP: {data.get('query')}")
        print(f"  Country: {data.get('country')}")
        print(f"  Country Code: {data.get('countryCode')}")
        print(f"  Region: {data.get('region')}")
        print(f"  Region Name: {data.get('regionName')}")
        print(f"  City: {data.get('city')}")
        print(f"  Zip: {data.get('zip')}")
        print(f"  Latitude: {data.get('lat')}")
        print(f"  Longitude: {data.get('lon')}")
        print(f"  Timezone: {data.get('timezone')}")
        print(f"  ISP: {data.get('isp')}")
        print(f"  Organization: {data.get('org')}")
        print(f"  AS: {data.get('as')}")
        print(f"  Mobile: {data.get('mobile')}")
        print(f"  Proxy: {data.get('proxy')}")
        print(f"  Hosting: {data.get('hosting')}")
        print(f"  Status: {data.get('status')}")
        with open("ip_log.txt", "a") as f:
         f.write(json.dumps(data, indent=4))  
         f.write("\n\n")  


    except Exception as e:
        print(f"[ERROR] {e}")

def ip_validate(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

if platform.system() == "Windows":
    os.system("cls")
elif platform.system() == "Linux":
    os.system("clear")

init()
Cursor.HideCursor()
whoami = os.getlogin()

print(Center.XCenter("""
███████╗██╗  ██╗ ██████╗ ██╗    ██╗███╗   ███╗███████╗████████╗██╗  ██╗███████╗██╗██████╗ 
██╔════╝██║  ██║██╔═══██╗██║    ██║████╗ ████║██╔════╝╚══██╔══╝██║  ██║██╔════╝██║██╔══██╗
███████╗███████║██║   ██║██║ █╗ ██║██╔████╔██║█████╗     ██║   ███████║█████╗  ██║██████╔╝
╚════██║██╔══██║██║   ██║██║███╗██║██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██╔══╝  ██║██╔═══╝ 
███████║██║  ██║╚██████╔╝╚███╔███╔╝██║ ╚═╝ ██║███████╗   ██║   ██║  ██║███████╗██║██║     
╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝ ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝╚═╝ 
                        Internet Protocol Show Information
                              [Author: know56_All1]
                    [Github: https://github.com/know56All1]
"""))

user_input = input(f"""ENTER THE IP OF THE VICTIM
                 
┌──(root@{whoami})-[SMI]
└─# """).strip()

if user_input == "exit":
    exit()

if not ip_validate(user_input):
    print(Fore.LIGHTRED_EX + "[ERROR] The indicated IP is not valid")
    exit()

requesting(user_input)
