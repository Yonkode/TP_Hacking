import socket
import sys
from datetime import datetime
import subprocess

subprocess.call("clear", shell = True)

remoteServerIP = input("Enter l'IP d'un serveur a scanner : ")

print("-"*60)
print("Lancement du scan des ports de la machine " + remoteServerIP)
print("-"*60)

t1 = datetime.now()

try:
    for port in range(1, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print(f"Port {port}:  Ouvert")
        sock.close()
except KeyboardInterrupt:
    print("Vous avez appuye sur Ctrl+c")
    sys.exit()
except socket.error:
    print("Impossible de se connecter au serveur ")
    sys.exit()

t2 = datetime.now()

total = t2 - t1

print(f"Scan complete en : {str (total)}")




