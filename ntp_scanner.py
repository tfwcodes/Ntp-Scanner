from ntplib import *
from time import sleep
import threading


def check_ntp(addr):
    try:
        server = NTPClient()
        server.request(addr, version=3)
        print("[+] NTP is enabled on {}".format(addr))
    except NTPException:
        print("[-] NTP is disabled on {}".format(addr))

is2 = input(f"[+] Do you want to scan multiple ip's/domains or just a single ip/domain [1/2]: ")
if is2 == "1":
    addr = input("[+] Enter the list with the ip's/domains: ")
    with open(addr, "r") as file:
        for line in file.readlines():
            ip_to_check = line.strip()
            
            t = threading.Thread(target=check_ntp, args=(ip_to_check, ))
            t.start()
            sleep(0.5)

elif is2 == "2":
    ntp = input("[+] Enter the ip/domain: ")
    check_ntp(ntp)
else:
    print("[-] The mode does not exists: ")