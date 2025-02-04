import socket
from IPy import IP
import concurrent.futures

t = input("[+] enter your target : ")


def chk(pi):
    try:
        IP(t)
    except ValueError:
        socket.gethostbyname(pi)
    return (pi)


def bann(sk):
    try:
        return sk.recv(1024)
    except:
        pass


def scn(t, po):
    try:
        sk = socket.socket()
        sk.settimeout(0.5)
        sk.connect((t, po))
        try:
            banner = bann(sk)
            if banner:
                print(f"[+] port {po} is open : {banner.decode().strip()}")
            else:
                print(
                    f"[+] port {po} is open but there is no banner found :( ")

        except Exception as e:
            print(f"[+] port {po} is open, but banner retrival failed: {e}")

    except:
        pass


ask = input("[+] do you want full scan 1 - 65xxx ? (y or n)")

conv = chk(t)

if ask.lower() == "y":
    start, end = 1, 65535
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(lambda p: scn(conv, p), range(start, end + 1))
else:
    try:
        start = int(input("[+] enter starting number"))
        end = int(input("[+] enter ending number"))
        for p in range(start, end):
            scn(conv, p)
    except ValueError:
        print("[!] Invalid port range input. Using default range 1-100.")
        start_port, end_port = 1, 100
